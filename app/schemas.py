# app/schemas.py
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from .models import PyObjectId

class BookCreate(BaseModel):
    title: str
    author: str
    published_date: str
    isbn: str

class BookUpdate(BaseModel):
    title: Optional[str]
    author: Optional[str]
    published_date: Optional[str]
    isbn: Optional[str]

class BookResponse(BookCreate):
    id: PyObjectId = Field(default_factory=PyObjectId, alias='_id')

    class Config:
        json_encoders = {
            PyObjectId: str
        }

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias='_id')
    username: str
    email: EmailStr

    class Config:
        json_encoders = {
            PyObjectId: str
        }

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str

# Define UserOut here if needed
class UserOut(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias='_id')
    username: str
    email: EmailStr