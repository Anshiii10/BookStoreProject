# app/main.py
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import timedelta
from .routes import router
from .config import load_config
from .database import connect_to_mongo, close_mongo_connection
from .schemas import BookCreate, BookResponse, BookUpdate, UserCreate, UserResponse, Token
from .crud import get_books, get_book, create_book, update_book, delete_book, create_user
from .auth import authenticate_user, create_access_token, get_current_user
from .dependencies import get_current_active_user

app = FastAPI()

# Load configuration
config = load_config()

# Connect to MongoDB
@app.on_event("startup")
async def startup_event():
    connect_to_mongo()

@app.on_event("shutdown")
async def shutdown_event():
    close_mongo_connection()

# Include routes
app.include_router(router)

@app.post("/register", response_model=UserResponse)
async def register(user: UserCreate):
    created_user = await create_user(user)
    return created_user

@app.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/books", response_model=list[BookResponse])
async def read_books():
    books = await get_books()
    return books

@app.get("/books/{id}", response_model=BookResponse)
async def read_book(id: str):
    book = await get_book(id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.post("/books", response_model=BookResponse)
async def create_book(book: BookCreate, current_user: UserResponse = Depends(get_current_active_user)):
    return await create_book(book)

@app.put("/books/{id}", response_model=BookResponse)
async def update_book(id: str, book: BookUpdate, current_user: UserResponse = Depends(get_current_active_user)):
    updated_book = await update_book(id, book)
    if updated_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated_book

@app.delete("/books/{id}")
async def delete_book(id: str, current_user: UserResponse = Depends(get_current_active_user)):
    await delete_book(id)
    return {"message": "Book deleted"}
