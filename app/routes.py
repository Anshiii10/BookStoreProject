from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from typing import List
from .database import book_collection
from .dependencies import get_current_active_user
from .schemas import UserCreate, UserOut, Token, BookCreate, BookUpdate, UserResponse
from .models import Book,User
from .auth import authenticate_user, create_access_token, get_password_hash, verify_password, get_current_active_user
from .database import db
from bson import ObjectId
from app.models import Book
from app.schemas import BookCreate, BookUpdate, UserCreate, UserResponse, Token, TokenData, UserOut


router = APIRouter()

# GET /books: Retrieve a list of all books
@router.get("/books", response_model=List[Book])
async def read_books():
    books = await db.books.find().to_list(1000)
    return books

# GET /books/{id}: Retrieve a specific book by its ID
@router.get("/books/{id}", response_model=Book)
async def read_book(id: str):
    book = await db.books.find_one({"_id": ObjectId(id)})
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

# POST /books: Add a new book (authenticated users only)
@router.post("/books", response_model=Book, dependencies=[Depends(get_current_active_user)])
async def create_book(book: Book):
    book_dict = book.dict()
    result = await db.books.insert_one(book_dict)
    new_book = await db.books.find_one({"_id": result.inserted_id})
    return new_book

# PUT /books/{id}: Update an existing book by its ID (authenticated users only)
@router.put("/books/{id}", response_model=Book, dependencies=[Depends(get_current_active_user)])
async def update_book(id: str, book: Book):
    update_result = await db.books.update_one({"_id": ObjectId(id)}, {"$set": book.dict()})
    if update_result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Book not found")
    updated_book = await db.books.find_one({"_id": ObjectId(id)})
    return updated_book

# DELETE /books/{id}: Delete a book by its ID (authenticated users only)
@router.delete("/books/{id}", response_model=Book, dependencies=[Depends(get_current_active_user)])
async def delete_book(id: str):
    deleted_book = await db.books.find_one_and_delete({"_id": ObjectId(id)})
    if deleted_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return deleted_book

# POST /register: Register a new user
@router.post("/register", response_model=UserOut)
async def register_user(user: UserCreate):
    existing_user = await db.users.find_one({"username": user.username})
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    hashed_password = get_password_hash(user.password)
    user_dict = user.dict()
    user_dict['hashed_password'] = hashed_password
    result = await db.users.insert_one(user_dict)
    new_user = await db.users.find_one({"_id": result.inserted_id})
    return new_user

@router.post("/login", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user['username']})
    return {"access_token": access_token, "token_type": "bearer"}