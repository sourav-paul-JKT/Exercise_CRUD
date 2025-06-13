# Exercise_CRUD

# 📚 FastAPI CRUD Application

This is a simple CRUD (Create, Read, Update, Delete) application built using **FastAPI**, **SQLite**, and **SQLAlchemy**. It manages a list of books with attributes like `title` and `author`.

---

## 🚀 Features

- Create a new book entry
- Read all books or a specific book by ID
- Update an existing book
- Delete a book
- Interactive API documentation via Swagger UI

---

## 🧰 Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/) — High-performance API framework
- [SQLAlchemy](https://www.sqlalchemy.org/) — ORM for database operations
- [SQLite](https://www.sqlite.org/index.html) — Lightweight database
- [Pydantic](https://docs.pydantic.dev/) — Data validation and schema creation

---

## 📂 Project Structure



Exercise_CRUD/

│
├── main.py # FastAPI app and route definitions

├── crud.py # CRUD operation logic

├── models.py # SQLAlchemy models

├── schemas.py # Pydantic schemas

├── database.py # Database connection setup

├── test.db # SQLite database file

├── requirements.txt # List of required dependencies

└── .gitignore # Files/folders to be ignored by Git


---

## 🧪 How to Run

### 1.Clone the repo

```bash
git clone https://github.com/sourav-paul-JKT/Exercise_CRUD.git
cd Exercise_CRUD

python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 2. Create and Activate a Virtual Environment

```
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Install Dependencies
```
pip install -r requirements.txt
```
### 4. Run the Application
```
uvicorn main:app --reload
```
### 5. Open Browser

Visit http://127.0.0.1:8000/docs to access the interactive Swagger UI.

## 🗃️ Example API Endpoints
POST /books/ — Create a book

GET /books/ — Get all books

GET /books/{id} — Get a specific book

PUT /books/{id} — Update a book

DELETE /books/{id} — Delete a book

