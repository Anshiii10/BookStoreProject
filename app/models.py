# app/models.py
from pydantic import BaseModel, Field
from bson import ObjectId
from typing import Optional
from datetime import datetime
from decimal import Decimal

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError('Invalid ObjectId')
        return ObjectId(v)

    def __repr__(self):
        return f"<PyObjectId {self}>"

# Define the Book model
class Book(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    title: str
    author: str
    published_date: str
    isbn: str

    class Config:
        json_encoders = {
            PyObjectId: str,
            datetime: lambda v: v.isoformat(),
            Decimal: lambda v: float(v),
        }

# Define the User model
class User(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    username: str
    email: str
    hashed_password: str

    class Config:
        allow_population_by_field_name = True
        json_encoders = {
            PyObjectId: str
        }
        schema_extra = {
            "example": {
                "username": "user1",
                "email": "user1@example.com",
                "hashed_password": "hashedpassword"
            }
        }
