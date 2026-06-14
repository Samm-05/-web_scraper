from database.db import SessionLocal
from database.models import Book

db = SessionLocal()

books = db.query(Book).all()

print(f"Total Books: {len(books)}")

for book in books[:10]:
    print(
        book.id,
        book.title,
        book.price
    )

db.close()