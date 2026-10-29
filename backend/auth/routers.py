from fastapi import APIRouter,Depends
from typing import Annotated
from sqlalchemy.orm import Session
from backend.auth import controller
from .schema import userLogin,userRegister,verifyCode,resetPassword
from backend.config.db_config import get_session


router = APIRouter(
    prefix="/api/auth",
    tags=["auth"]
)

@router.post("/login")
async def login(user:userLogin,session:Annotated[Session,Depends(get_session)]):
   
    return await controller.login(user,session)

@router.post("/register")
async def register(user:userRegister,session:Annotated[Session,Depends(get_session)]):
    return await controller.register(user,session)

@router.post("/resetpassword")
async def reset_password(obj:resetPassword,session:Annotated[Session,Depends(get_session)]):
    return await controller.reset_password(obj,session)

@router.post("/verifycode")
async def verify_code(obj:verifyCode,session:Annotated[Session,Depends(get_session)]):
    return await controller.verify_code(obj,session)