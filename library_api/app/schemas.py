from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: str
    is_active: bool = True
    
    class Config:
        orm_mode = True

class BookBase(BaseModel):
    title: str
    author: str

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: str
    is_available: bool = True
    
    class Config:
        orm_mode = True

class BorrowRecordBase(BaseModel):
    user_id: str
    book_id: str

class BorrowRecordCreate(BorrowRecordBase):
    pass

class BorrowRecord(BorrowRecordBase):
    id: str
    borrow_date: datetime
    return_date: Optional[datetime]

    class Config:
        orm_mode = True
