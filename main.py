from typing import List

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import models
import crud
import schemas
from database import SessionLocal, engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/books/", response_model=List[schemas.Book])
def list_books(
        db: Session = Depends(get_db),
        skip: int = 0,
        limit: int = 10,
        author_id: int = None,
):
    return crud.get_all_books(
        db=db,
        skip=skip,
        limit=limit,
        author_id=author_id
    )


@app.post("/books/", response_model=schemas.Book)
def create_book(
        book: schemas.BookCreate,
        db: Session = Depends(get_db),
):
    return crud.create_book(db=db, book=book)

@app.get("/authors/", response_model=List[schemas.Author])
def list_authors(
        db: Session = Depends(get_db),
        skip: int = 0,
        limit: int = 10,
):
    return crud.get_all_authors(db=db, skip=skip, limit=limit)

@app.post("/authors/", response_model=schemas.Author)
def create_author(
        author: schemas.AuthorCreate,
        db: Session = Depends(get_db),
):
    return crud.create_author(db=db, author=author)

@app.get("/authors/{id}/", response_model=schemas.Author)
def get_one_author(
        id: int,
        db: Session = Depends(get_db)
):
    return crud.get_author(db=db, id=id)