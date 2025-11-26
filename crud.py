from typing import List

from fastapi import HTTPException
from sqlalchemy.orm import Session

import models
from schemas import BookCreate, AuthorCreate, AuthorUpdate, BookUpdate


def get_all_books(
        db: Session,
        skip: int = 0,
        limit: int = 10,
        author_id: int = None
) -> List[models.Book]:
    query = db.query(models.Book)

    if author_id is not None:
        query = query.filter(models.Book.author_id == author_id)

    db_books = query.offset(skip).limit(limit).all()

    if not db_books:
        return []

    return db_books

def create_book(db: Session, book: BookCreate):
    db_book = models.Book(**book.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_book(db: Session, id: int):
    return db.query(models.Book).filter(models.Book.id == id).first()

def update_book(db: Session, id: int, book: BookUpdate):
    db_book = get_book(db, id)

    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")

    book_data = book.model_dump(exclude_unset=True)

    for key, value in book_data.items():
        setattr(db_book, key, value)

    db.commit()
    db.refresh(db_book)
    return db_book

def delete_book(db: Session, id:int):
    db_book = get_book(db, id)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(db_book)
    db.commit()
    return f"Book with id {id} was deleted"

def get_all_authors(db: Session, skip: int = 0, limit: int = 10):
    db_author = db.query(models.Author).offset(skip).limit(limit).all()
    if not db_author:
        return []
    return db_author

def get_author(db: Session, id: int):
    db_author = db.query(models.Author).filter(models.Author.id == id).first()
    if not db_author:
        raise HTTPException(status_code=404, detail="Author not found")
    return db_author

def create_author(db:Session, author: AuthorCreate):
    db_author = models.Author(**author.model_dump())
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author

def update_author(db: Session, id: int, author: AuthorUpdate):
    db_author = get_author(db, id)
    if not db_author:
        raise HTTPException(status_code=404, detail="Author not found")

    author_data = author.model_dump(exclude_unset=True)
    for key, value in author_data.items():
        setattr(db_author, key, value)

    db.commit()
    db.refresh(db_author)
    return db_author

def delete_author(db: Session, id: int):
    db_author = get_author(db, id)
    if not db_author:
        raise HTTPException(status_code=404, detail="Author not found")
    db.delete(db_author)
    db.commit()
    return f"Author with id {id} was deleted"
