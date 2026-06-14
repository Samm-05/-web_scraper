from sqlalchemy.orm import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

Base = declarative_base()


class Book(Base):

    __tablename__ = "books"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    title = Column(
        String,
        unique=True,
        nullable=False
    )

    price = Column(
        String,
        nullable=False
    )