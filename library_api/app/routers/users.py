from fastapi import APIRouter, HTTPException, status
from typing import List
from ..import crud, schemas

router = APIRouter()

@router.post("/users", response_model=schemas.User, status_code=201)
def create_user(user_create: schemas.UserCreate):
    try:
        new_user = crud.create_user(user_create)
        if not new_user: 
            raise HTTPException(status_code=400, detail="User creation failed.")
        return new_user
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{user_id}", response_model=schemas.User)
def read_user(user_id: str):
    get_user = crud.get_user(user_id)
    if get_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    return get_user

@router.put("/{user_id}", response_model=schemas.User)
def update_user(user_id: str, user: schemas.UserCreate):
    updated_user = crud.update_user(user_id, user.name, user.email)
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    return updated_user