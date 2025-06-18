from sqlalchemy import Column, Integer, String
from database import Base

class Book(Base):
    """
    SQLAlchemy ORM model for the 'books' table.
    Attributes:
        id (int): Primary key, unique identifier for each book.
        title (str): Title of the book.
        author (str): Author of the book.
    """
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)

