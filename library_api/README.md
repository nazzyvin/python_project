# Library API

## Overview
The Library API is a FastAPI-based server that allows users to manage an online library system. The API supports operations like creating users, managing books, borrowing and returning books, and tracking borrow records.

## Features
- **User Management**: Create, update, deactivate, and retrieve user details.
- **Book Management**: Add, update, mark unavailable, and retrieve book details.
- **Borrowing System**: Borrow books, return borrowed books, and view borrow records.
- **API Versioning**: `/api/v1` prefix for versioning the API endpoints.

## Project Structure
```
library_api/
├── app/
│   ├── crud.py        # Business logic for CRUD operations
│   ├── main.py        # Entry point for the FastAPI application
│   ├── models.py      # Data models for Users, Books, and BorrowRecords
│   ├── schemas.py     # Pydantic schemas for request and response validation
│   ├── routers/       # Router modules for Users, Books, and BorrowRecords
│   │   ├── __init__.py
│   │   ├── books.py
│   │   ├── users.py
│   │   └── borrow_records.py
│   └── __init__.py
└── README.md         # Project documentation
```

## Prerequisites
- Python 3.8+
- pip (Python package installer)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/library-api.git
   cd library-api
   ```

2. Create a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate    # On Windows: .\env\Scripts\activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```

## API Endpoints

### Root Endpoint
- **GET** `/` - Welcome message

### User Routes
- **POST** `/api/v1/users` - Create a new user
- **GET** `/api/v1/users/{user_id}` - Retrieve a user by ID
- **PUT** `/api/v1/users/{user_id}` - Update a user's name or email

### Book Routes
- **POST** `/api/v1/books` - Add a new book
- **GET** `/api/v1/books/{book_id}` - Retrieve a book by ID
- **PUT** `/api/v1/books/{book_id}` - Update a book's details
- **PATCH** `/api/v1/books/{book_id}/unavailable` - Mark a book as unavailable

### Borrow Records Routes
- **POST** `/api/v1/borrow-records/borrow` - Borrow a book
- **POST** `/api/v1/borrow-records/return/{borrow_record_id}` - Return a borrowed book
- **GET** `/api/v1/borrow-records/user/{user_id}` - Retrieve borrow records for a user
- **GET** `/api/v1/borrow-records` - Retrieve all borrow records

## Project Goals
The primary objective is to deliver a modular, efficient API for managing a library system. The use of FastAPI ensures high performance and ease of development.

## License
This project is licensed under the [MIT License](LICENSE).