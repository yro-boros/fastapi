from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel

app = FastAPI()

books = [
    {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"},
    {"id": 3, "title": "1984", "author": "George Orwell"},    
    {"id": 4, "title": "The Cat in the Hat", "author": "Dr. Seuss"}   
]

class Book(BaseModel):
    title: str
    author: str

@app.get("/items", tags=["Книги"], summary="Получение списка всех книг")
def read_root():
    return books

@app.get("/items/{item_id}", tags=["Узнать за книгу"], summary="Получение одной книги по id")
def read_item(item_id: int):
    for book in books:
        if book["id"] == item_id:
            return book
    raise HTTPException(status_code=404, detail="Нет такого значения")

@app.post("/items", tags=["Добавить книгу"], summary="Добавление новой книги")
def create_item(book: Book):
    books.append({
        "id": len(books) + 1,
        "title": book.title,
        "author": book.author
    })
    return books[-1]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)