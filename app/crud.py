# app/crud.py
from .database import db
from .models import Book, User
from .schemas import BookCreate, BookUpdate, UserCreate
from .auth import get_password_hash
from bson import ObjectId

async def get_books():
    books = await db.books.find().to_list(1000)
    return books

async def get_book(book_id: str):
    return await db.books.find_one({"_id": ObjectId(book_id)})

async def create_book(book: BookCreate):
    new_book = await db.books.insert_one(book.dict())
    created_book = await get_book(new_book.inserted_id)
    return created_book

async def update_book(book_id: str, book: BookUpdate):
    await db.books.update_one({"_id": ObjectId(book_id)}, {"$set": book.dict(exclude_unset=True)})
    updated_book = await get_book(book_id)
    return updated_book

async def delete_book(book_id: str):
    await db.books.delete_one({"_id": ObjectId(book_id)})

async def create_user(user: UserCreate):
    hashed_password = get_password_hash(user.password)
    user_dict = user.dict()
    user_dict['hashed_password'] = hashed_password
    del user_dict['password']
    new_user = await db.users.insert_one(user_dict)
    created_user = await db.users.find_one({"_id": new_user.inserted_id})
    return created_user
