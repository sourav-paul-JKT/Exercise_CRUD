# Exercise_CRUD
 
# FastAPI CRUD Application
 
This is a simple CRUD (Create, Read, Update, Delete) application built using **FastAPI**, **SQLite**, and **SQLAlchemy**. It manages a list of books with attributes like `title` and `author`.
 
---
 
## Features
 
- Create a new book entry
- Read all books or a specific book by ID
- Update an existing book
- Delete a book
- User authentication: Signup and Login (username + password)
- Interactive API documentation via Swagger UI
- Dockerized for easy deployment
- Supports `.env` for configuration
 
---
 
## Tech Stack
 
- **FastAPI** — Web framework
- **SQLAlchemy** — ORM
- **SQLite** — Lightweight DB
- **Pydantic** — Data validation
- **Docker** — Containerization
- **Python-dotenv** — Load environment variables
 
---
 
## Project Structure
 
 
Exercise_CRUD/
 
│
├── main.py # FastAPI app entrypoint
 
├── crud.py # Business logic
 
├── models.py # DB models
 
├── schemas.py # Pydantic schemas
 
├── database.py # DB connection setup

├── middleware/

│ └── auth.py # Signup/Login routes & auth logic
 
├── requirements.txt # Project dependencies
 
├── Dockerfile # Docker build instructions
 
├── .dockerignore # Files to exclude from Docker build
 
├── .env # Environment config
 
 
---
 
## Run the Project Anywhere with Docker
 
>  Prerequisite: Make sure [Docker is installed](https://docs.docker.com/get-docker/)
 
###  Step 1: Clone the Repository
 
```bash
git clone https://github.com/sourav-paul-JKT/Exercise_CRUD.git
cd Exercise_CRUD
```
### step 2: Create a .env File
In the root directory of the project, create a .env file with the following content:
```
# .env

DATABASE_URL=sqlite:///./test.db
SECRET_KEY=your_super_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

```

###  Step 3: Build the Docker Image
 
```
docker build -t fastapi-crud-app .
```
 
### Step 4: Run the Container
```
docker run -d -p 8000:8000 --env-file .env fastapi-crud-app
 
```
### step 5: Open Browser
 
Visit http://127.0.0.1:8000/docs or  http://localhost:8000/docs to access the interactive Swagger UI.

## Auth API Endpoints
POST	/signup 	-Register a user
POST	/login 	 -Login with password
 
## Book API Endpoints
POST /books/ — Create a book
 
GET /books/ — Get all books
 
GET /books/{id} — Get a specific book
 
PUT /books/{id} — Update a book
 
DELETE /books/{id} — Delete a book
