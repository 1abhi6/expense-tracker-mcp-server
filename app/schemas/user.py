from pydantic import BaseModel, EmailStr
from datetime import datetime


class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserCreate(UserBase):
    password: str  # plain password for registration


class UserOut(UserBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
