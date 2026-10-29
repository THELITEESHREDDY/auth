from typing import Annotated
from fastapi import Depends, HTTPException,status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta,datetime, timezone

from backend.auth.schema import Token, resetPassword, userLogin, userRegister, verifyCode, User
from backend.config.jwt_process import authenticate_user,create_access_token
from backend.config.settings import settings

async def login(
    session:Session,
    req_user:userLogin
)->Token:
    user = authenticate_user(session,req_user.email, req_user.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate":"Bearer"}
        )

    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")


async def register(user:userRegister,session:Session):
    user_dict = user.model_dump()

    if user_dict.get("username","")=="" or user_dict.get("email","")=="" or user_dict.get('password',"")=="":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid field values"
        )

    new_user = User(
        username=user_dict['username'],
        password=user_dict['password'],
        email=user_dict['email']
    )

    try:
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
    except RuntimeError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Something bad with database, retry later"
        )

    #redirect to login
    return user_dict


async def reset_password(user:resetPassword,session:Session):
    user_dict = user.model_dump()
    
    return user_dict


async def verify_code(user:verifyCode,session:Session):
    user_dict = user.model_dump()
    
    return user_dict