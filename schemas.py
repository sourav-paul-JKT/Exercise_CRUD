from pydantic import BaseModel

class BookBase(BaseModel):
    """
    Shared base schema for Book.
    Attributes:
        title (str): Title of the book.
        author (str): Author of the book.
    """
    title: str
    author: str

class BookCreate(BookBase):
    """
    Schema for creating a new book.
    Inherits all fields from BookBase.
    """
    pass

class Book(BookBase):
    """
    Schema for reading (returning) a book.
    Inherits all fields from BookBase, and adds:
    Attributes:
        id (int): Unique identifier of the book.
    """
    id: int

    class Config:
        
        from_attributes = True


class UserCreate(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    username: str
    class Config:
        orm_mode = True

