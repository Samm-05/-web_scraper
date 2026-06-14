from database.db import SessionLocal
from database.models import Book


def save_books(books):

    db = SessionLocal()

    try:

        for item in books:

            existing_book = (
                db.query(Book)
                .filter(
                    Book.title == item["title"]
                )
                .first()
            )

            if not existing_book:

                new_book = Book(
                    title=item["title"],
                    price=item["price"]
                )

                db.add(new_book)

        db.commit()

    except Exception as e:

        print(
            f"Database Error: {e}"
        )

        db.rollback()

    finally:

        db.close()