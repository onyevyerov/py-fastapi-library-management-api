from datetime import date

from pydantic import BaseModel



class AuthorBase(BaseModel):
    name: str
    bio: str

    model_config = {
        "from_attributes": True
    }


class AuthorCreate(AuthorBase):
    pass


class AuthorUpdate(AuthorBase):
    pass


class Author(AuthorBase):
    id: int

    model_config = {
        "from_attributes": True
    }


class BookBase(BaseModel):
    title: str
    summary: str | None = None
    author_id: int
    model_config = {
        "from_attributes": True
    }
    publication_date: date
    author_id: int

    model_config = {
        "from_attributes": True
    }


class Book(BookBase):
    id: int

    model_config = {
        "from_attributes": True
    }

class BookCreate(BookBase):
    pass


class BookUpdate(BookBase):
    pass

