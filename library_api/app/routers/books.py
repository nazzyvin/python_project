# app/routers/books.py
from fastapi import APIRouter, HTTPException
from typing import List
import uuid
from .. import crud, schemas

router = APIRouter()

@router.post("/", response_model=schemas.Book)
def create_book(book: schemas.BookCreate):
    new_book = schemas.Book(id=str(uuid.uuid4()), title=book.title, author=book.author)
    return new_book

@router.get("/{book_id}", response_model=schemas.Book)
def read_book(book_id: str):
    book = crud.get_book(book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    
    return book

@router.put("/{book_id}", response_model=schemas.Book)
def update_book(book_id: str, book: schemas.BookCreate):
    updated_book = crud.update_book(book_id, book.title, book.author)
    if updated_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    
    return updated_book

@router.patch("/{book_id}/unavailable", response_model=schemas.Book)
def mark_book_unavailable(book_id: str):
    book = crud.mark_book_unavailable(book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    
    return book