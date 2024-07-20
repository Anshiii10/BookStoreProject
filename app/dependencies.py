# app/dependencies.py
from fastapi import Depends, HTTPException, status
from .auth import get_current_user
from .models import User

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    return current_user
