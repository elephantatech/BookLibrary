from typing import Optional
from datetime import datetime
from pydantic import BaseModel


class book(BaseModel):
    """This is model for each book"""

    title: str
    book_synopsis: Optional[str] = None
    author: str
    published_date: datetime
    edition: str
    ISDN_number: Optional[str] = None
    comments: Optional[str] = None


class response_book(book):
    """Response model for book object with the id"""

    id: str
