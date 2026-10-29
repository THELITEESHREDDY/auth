from uuid import uuid4
from typing import Annotated
from fastapi import Depends, HTTPException,status
from sqlalchemy.orm import Session
from sqlalchemy import select, update
from datetime import timedelta,datetime, timezone
from fastapi_mail import NameEmail

from backend.auth.model import User
from backend.auth.schema import Token, resetPassword, userLogin, userRegister, verifyCode
from backend.config.jwt_process import authenticate_user,create_access_token, get_password_hash
from backend.config.settings import settings
from backend.utils.emailService import simple_send
async def login(
    req_user:userLogin,
    session:Session
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

    is_existing_user = session.scalars(select(User).where(User.email==user.email or User.username==user.username)).first()

    if is_existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="username or email already exists"
        )

    new_user = User(
            id=str(uuid4()),
            username=user_dict['username'],
            hashed_password=get_password_hash(user_dict['password']),
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
    #email_user = NameEmail(name=new_user.username,email=new_user.email)
    return {"status" : 200 , "message":"registered successfull"}
    


async def reset_password(user:resetPassword,session:Session):
    user_dict = user.model_dump()

    existing_user = session.scalars(select(User).where(User.username==user.username and User.email==user.email)).first()

    if not existing_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Sorry! We aren't able to find you!"
        )

    update_user = session.execute(update(User).where(User.username==user.username and User.email==user.email).values(hashed_password=get_password_hash(user.new_password)))
    
    session.commit()
    
    return {"status" : 200 , "message":"reset successfull"}


async def verify_code(user:verifyCode,session:Session):
    user_dict = user.model_dump()
    
    return user_dict