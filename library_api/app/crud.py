from typing import List, Optional
import uuid
from .models import User, Book, BorrowRecord
from .schemas import UserCreate, User
from datetime import date

users: List[User] = []
books: List[Book] = []
borrow_records: List[BorrowRecord] = []

def create_user(user_create: UserCreate) -> User:
    for u in users:
        if u.email == user_create.email:
            raise ValueError("User with this email already exits")
        
    new_user = User(id=str(uuid.uuid4()), **user_create.dict())
    users.append(new_user)
    return new_user
    
def get_user(user_id: str) -> Optional[User]:
    for u in users:
        if u.id == user_id:
            return u
    
    return None

def update_user(user_id: str, name: str, email: str) -> Optional[User]:
    user = get_user(user_id)
    if user:
        user.name = name
        user.email = email
        return user
    
    return None

def deactivate_user(user_id: str) -> Optional[User]:
    user = get_user(user_id)
    if user:
        user.is_active = False
    return user

def create_book(book: Book) -> Book:
    books.append(book)
    return book

def get_book(book_id: str) -> Optional[Book]:
    for b in books:
        if b.id == book_id:
            return b
        
    return None

def update_book(book_id: str, title: str, author: str) -> Optional[Book]:
    book = get_book(book_id)
    if book:
        book.title = title
        book.author = author
        return book
    
    return None

def mark_book_unavailable(book_id: str) -> Optional[Book]:
    book = get_book(book_id)
    if book:
        book.is_available = False
        return book
    
    return None

def borrow_book(user_id: str, book_id: str) -> Optional[BorrowRecord]:
    user = get_user(user_id)
    book = get_book(book_id)
    if user and user.is_active and book and book.is_available:
        if not any(
            br for br in borrow_records
            if br.user_id == user_id and br.book_id == book_id and br.return_date is None
            ):
            borrow_record = BorrowRecord(
            id=str(uuid.uuid4()),
            user_id=user_id,
            book_id=book_id,
            borrow_date=date.today()
            )
            borrow_records.append(borrow_record)
            book.is_available = False
            return borrow_record
        
    return None

def return_book(borrow_record_id: str) -> Optional[BorrowRecord]:
    borrow_record = next((br for br in borrow_records if br.id == borrow_record_id), None)
    if borrow_record and borrow_record.return_date is None:
        borrow_record.return_date = date.today()
        book = get_book(borrow_record.book_id)
        if book:
            book.is_available = True
        else:
            print(f"Error: Book with ID {borrow_record.book_id} not found when returning the book.")
        
        return borrow_record
    return None

def get_borrow_records_by_user(user_id: str) -> List[BorrowRecord]:
    user_borrow_records = [br for br in borrow_records if br.user_id == user_id]
    if not user_borrow_records:
        pass

    return user_borrow_records

def get_all_borrow_records() -> List[BorrowRecord]:
    if not borrow_records:
        pass
    
    return borrow_records