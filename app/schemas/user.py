from pydantic import BaseModel, EmailStr, Field, ConfigDict
from enum import Enum


class UserType(str, Enum):
    student = "student"
    teacher = "professor"
    admin = "admin"

class UserBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    type: UserType

class UserCreate(UserBase):
    password: str = Field(..., min_length=8, max_length=64)

class UserResponse(UserBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
