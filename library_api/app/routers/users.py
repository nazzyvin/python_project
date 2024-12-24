# app/routers/users.py
from fastapi import APIRouter, HTTPException
from typing import List
from ..import crud, schemas

router = APIRouter()

@router.post("/", response_model=schemas.User)
def create_user(user: schemas.UserCreate):
    new_user = crud.create_user(user)
    
    return new_user

@router.get("/{user_id}", response_model=schemas.User)
def read_user(user_id: str):
    user = crud.get_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user

@router.put("/{user_id}", response_model=schemas.User)
def update_user(user_id: str, user: schemas.UserCreate):
    updated_user = crud.update_user(user_id, user)