
from fastapi import APIRouter, HTTPException
from typing import List
from datetime import date
from .. import crud, schemas

router = APIRouter()

@router.post("/borrow/", response_model=schemas.BorrowRecord)
def borrow_book(borrow_data: schemas.BorrowRecordCreate):
    borrow_record = crud.borrow_book(borrow_data.user_id, borrow_data.book_id)
    if borrow_record is None:
        raise HTTPException(status_code=400, detail="Book unavailable or user inactive")
    return borrow_record

@router.post("/return/{borrow_record_id}", response_model=schemas.BorrowRecord)
def return_book(borrow_record_id: str):
    borrow_record = crud.return_book(borrow_record_id)
    if borrow_record is None:
        raise HTTPException(status_code=404, detail="Borrow record not found or book already returned")
    return borrow_record

@router.get("/user/{user_id}", response_model=List[schemas.BorrowRecord])
def get_user_borrow_records(user_id: str):
    return crud.get_borrow_records_by_user(user_id)

@router.get("/", response_model=List[schemas.BorrowRecord])
def get_all_borrow_records():
    return crud.get_all_borrow_records()