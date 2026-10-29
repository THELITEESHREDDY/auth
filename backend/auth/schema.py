from pydantic import BaseModel,EmailStr

class User(BaseModel):
    username:str|None
    email:str|None
    password:str
    disabled: bool | None = None


class userLogin(User):
    pass

class userRegister(User):
    pass

class resetPassword(BaseModel):
    email:EmailStr

class verifyCode(BaseModel):
    code:str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None


class UserInDB(User):
    hashed_password: str