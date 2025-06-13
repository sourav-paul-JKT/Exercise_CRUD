from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud
from database import SessionLocal, engine

# Create database tables if they don't exist
models.Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI()

def get_db():
    """
    Dependency function to get a SQLAlchemy database session.
    Closes the session automatically after request is complete.
    Yields:
        Session: SQLAlchemy database session.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/books/", response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    """
    API endpoint to create a new book.
    Args:
        book (schemas.BookCreate): Book data from the request body.
        db (Session): SQLAlchemy database session.
    Returns:
        schemas.Book: The created book.
    """
    return crud.create_book(db=db, book=book)

@app.get("/books/", response_model=list[schemas.Book])
def read_books(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    API endpoint to retrieve multiple books with pagination.
    Args:
        skip (int, optional): Number of books to skip for pagination. Defaults to 0.
        limit (int, optional): Maximum number of books to return. Defaults to 10.
        db (Session): SQLAlchemy database session.
    Returns:
        List[schemas.Book]: List of books.
    """
    books = crud.get_books(db, skip=skip, limit=limit)
    return books

@app.get("/books/{book_id}", response_model=schemas.Book)
def read_book(book_id: int, db: Session = Depends(get_db)):
    """
    API endpoint to retrieve a single book by ID.
    Args:
        book_id (int): ID of the book to retrieve.
        db (Session): SQLAlchemy database session.
    Raises:
        HTTPException: 404 error if book is not found.
    Returns:
        schemas.Book: The retrieved book.
    """
    db_book = crud.get_book(db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

