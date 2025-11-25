from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Author(Base):
    __tablename__ = "authors"
    id = Column(
        Integer,
        primary_key=True,
        unique=True,
        index=True,
        autoincrement=True
    )
    name = Column(String(55), nullable=False, unique=True)
    bio = Column(String(610), nullable=True)
    books = relationship("Book", backref="author")

class Book(Base):
    __tablename__ = "books"
    id = Column(
        Integer,
        primary_key=True,
        unique=True,
        index=True,
        autoincrement=True
    )
    title = Column(String(55), nullable=False)
    summary = Column(String(255), nullable=True)
    publication_date = Column(Date)
    author_id = Column(Integer, ForeignKey("authors.id"))