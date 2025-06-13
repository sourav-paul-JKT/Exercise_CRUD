from sqlalchemy.orm import Session
import models, schemas

def get_book(db: Session, book_id: int):
    """
    Retrieve a single book by its ID.
    Args:
        db (Session): SQLAlchemy database session.
        book_id (int): The ID of the book to retrieve.
    Returns:
        models.Book or None: The book object if found, else None.
    """
    return db.query(models.Book).filter(models.Book.id == book_id).first()

def get_books(db: Session, skip: int = 0, limit: int = 10):
    """
    Retrieve a list of books with optional pagination.
    Args:
        db (Session): SQLAlchemy database session.
        skip (int, optional): Number of records to skip (for pagination). Defaults to 0.
        limit (int, optional): Maximum number of records to return. Defaults to 10.
    Returns:
        List[models.Book]: List of book objects.
    """
    return db.query(models.Book).offset(skip).limit(limit).all()

def create_book(db: Session, book: schemas.BookCreate):
    """
    Create a new book record.
    Args:
        db (Session): SQLAlchemy database session.
        book (schemas.BookCreate): The book data for creation.
    Returns:
        models.Book: The created book object.
    """
    db_book = models.Book(title=book.title, author=book.author)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

