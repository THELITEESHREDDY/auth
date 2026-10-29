from sqlalchemy import String
from sqlalchemy.orm import mapped_column,Mapped,DeclarativeBase
from pydantic import EmailStr


class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user_account"
    id:Mapped[str] = mapped_column(default=None,primary_key=True)
    username:Mapped[str] = mapped_column(String)
    email:Mapped[EmailStr] = mapped_column(String)
    hashed_password:Mapped[str] = mapped_column(String)