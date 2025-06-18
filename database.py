from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get database URL from environment or fallback to default
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")

# Create SQLAlchemy engine
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
"""
SQLAlchemy database engine.

Uses SQLite as the database, connecting to './test.db' or any path set via .env.
The 'check_same_thread' argument is set to False to allow connections from different threads,
which is necessary for SQLite when used with FastAPI.
"""

# Create a session factory for database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
"""
SQLAlchemy SessionLocal class.

- autocommit=False: Transactions are managed manually.
- autoflush=False: Disable automatic flush before queries.
- bind=engine: Binds the session to the engine created above.
"""

# Declarative base class for ORM models
Base = declarative_base()
"""
Base class for ORM models.

All SQLAlchemy models will inherit from this Base class to get the metadata and mapping functionality.
"""

def get_db():
    """
    Yields a SQLAlchemy database session.
    Automatically closes the session after request is complete.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
