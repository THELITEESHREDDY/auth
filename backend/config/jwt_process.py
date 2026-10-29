from datetime import datetime, timedelta, timezone
from typing import Annotated

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwt.exceptions import InvalidTokenError
from pwdlib import PasswordHash
from backend.config.settings import settings
from backend.config.db_config import get_session
from backend.auth.schema import Token,TokenData
from backend.auth.schema import User,UserInDB
from sqlalchemy.orm import Session
from sqlalchemy import select


password_hash = PasswordHash.recommended()

DUMMY_HASH = password_hash.hash("dummypassword")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def verify_password(plain_password,hashed_password):
    return password_hash.verify(plain_password,hashed_password)


def get_password_hash(password):
    return password_hash.hash(password)


def get_user(db:Session, email: str):
    user = db.scalar(select(User).where(User.email == email)).first()
    return UserInDB(user)


def authenticate_user(db:Annotated[Session,Depends(get_session)], email: str, password: str):
    user = get_user(db, email)
    if not user:
        verify_password(password,DUMMY_HASH)
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt





async def get_current_user(token:Annotated[str,Depends(oauth2_scheme)],db:Annotated[Session,Depends(get_session)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate":"Bearer"}
    )

    try:
        payload =jwt.decode(token,settings.SECRET_KEY,algorithms=settings.ALGORITHM)
        
        email = payload.get("sub")

        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)

    except InvalidTokenError:
        raise credentials_exception

    user = get_user(db,email=token_data.email)

    if user is None:
        raise credentials_exception

    return user


async def get_current_active_user(current_user:Annotated[User,Depends(get_current_user)]):

    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")

    return current_user


