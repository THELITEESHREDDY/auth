from pydantic import BaseModel,EmailStr,ConfigDict

class User(BaseModel):
    username:str|None
    email:str|None
    password:str
    disabled: bool | None = None
    model_config = ConfigDict(from_attributes=True)


class userLogin(User):
    pass

class userRegister(User):
    pass

class resetPassword(BaseModel):
    email:EmailStr
    username:str
    new_password:str

class verifyCode(BaseModel):
    code:str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None


class UserInDB(BaseModel):
    username:str|None
    email:str|None
    hashed_password: str