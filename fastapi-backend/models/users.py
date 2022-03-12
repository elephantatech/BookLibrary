from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional


class user(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr = Field(example="test@example.com")
    password: str = Field(min_length=3, max_length=28)
    phone: str
    comments: Optional[str] = None
    dob: datetime


class user_reponse(user):
    id: str

    def create_user(self):
        pass


class group(BaseModel):
    pass
