from pydantic import BaseModel, EmailStr
from typing import Optional


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str   
    is_admin: Optional[bool] = False


class UserUpdate(BaseModel):
    name: str = None
    email: str = None
