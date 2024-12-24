# app/models.py
from typing import Optional
from datetime import date

class User:
    def _init_(self, id: int, name: str, email: str, is_active: bool = True):
        self.id = id
        self.name = name
        self.email = email
        self.is_active = is_active

class Book:
    def _init_(self, id: int, title: str, author: str, is_available: bool = True):
        self.id = id
        self.title = title
        self.author = author
        self.is_available = is_available

class BorrowRecord:
    def _init_(self, id: int, user_id: int, book_id: int, borrow_date: date, return_date: Optional[date] = None):
        self.id = id
        self.user_id = user_id
        self.book_id = book_id
        self.borrow_date = borrow_date
        self.return_date = return_date
