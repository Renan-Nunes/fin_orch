from pydantic import BaseModel, EmailStr
from typing import Optional


class UserBase(BaseModel):
    name: str
    surname: Optional[str] = None
    email: EmailStr
    cpf: str


class UserCreate(UserBase):
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserUpdate(BaseModel):
    name: Optional[str] = None
    surname: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    cpf: Optional[str] = None


class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True
