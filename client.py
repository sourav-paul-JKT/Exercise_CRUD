import requests
import jwt
import getpass
 
API_BASE = "http://localhost:8000"
LOGIN_ENDPOINT = f"{API_BASE}/auth/login"
BOOKS_ENDPOINT = f"{API_BASE}/books/"
 
def login(username, password):
    response = requests.post(LOGIN_ENDPOINT, json={"username": username, "password": password})
    if response.status_code != 200:
        raise Exception(f"Login failed: {response.text}")
    return response.json()["access_token"]
 
def get_username_from_token(token):
    decoded = jwt.decode(token, options={"verify_signature": False})
    return decoded.get("sub")
 
def get_books_public():
    response = requests.get(BOOKS_ENDPOINT)
    return response.json()
 
def get_book_by_id_public(book_id):
    response = requests.get(f"{BOOKS_ENDPOINT}{book_id}")
    return response.json()
 
def create_book(token, title, author):
    headers = {"Authorization": f"Bearer {token}"}
    data = {"title": title, "author": author}
    response = requests.post(BOOKS_ENDPOINT, json=data, headers=headers)
    return response.json()
 
def update_book(token, book_id, title, author):
    headers = {"Authorization": f"Bearer {token}"}
    data = {"title": title, "author": author}
    response = requests.put(f"{BOOKS_ENDPOINT}{book_id}", json=data, headers=headers)
    return response.json()
 
def delete_book(token, book_id):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.delete(f"{BOOKS_ENDPOINT}{book_id}", headers=headers)
    return response.json()
 
if __name__ == "__main__":
    print("Fetching all books...")
    books = get_books_public()
    for book in books:
        print(f"- {book['id']}: {book['title']} by {book['author']}")
 
    if books:
        first_book_id = books[0]['id']
        print(f"Fetching book by ID ({first_book_id})...")
        book_detail = get_book_by_id_public(first_book_id)
        print(book_detail)
 
    print("\n Login to perform write operations")
    username = input("Username: ")
    password = getpass.getpass("Password: ")
 
    try:
        token = login(username, password)
        print("Logged in successfully.")
 
        user_from_token = get_username_from_token(token)
        print(f"Token belongs to: {user_from_token}")
 
        # Create a book
        print("\nCreating a book...")
        new_book = create_book(token, "The Alchemist", "Paulo Coelho")
        print("Created:", new_book)
 
        # Update the book
        print("\nUpdating the book...")
        updated_book = update_book(token, new_book["id"])
        print("Updated:", updated_book)
 
        # Delete the book
        print("\nDeleting the book...")
        deleted = delete_book(token, new_book["id"])
        print("Deleted:", deleted)
 
    except Exception as e:
        print("Error:", e)