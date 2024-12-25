from fastapi import FastAPI
from .routers import users, books, borrow_records

app = FastAPI()

app.include_router(books.router, prefix="/api/v1/books", tags=["Books Routes"])
app.include_router(users.router, prefix="/api/v1/users", tags=["Users Routes"])
app.include_router(borrow_records.router, prefix="/api/v1/borrow-records", tags=["Borrow Records Routes"])

@app.get("/")
def root():
    return {"message": "Welcome to the Library API"}
