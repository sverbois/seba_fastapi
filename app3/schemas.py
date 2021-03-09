import datetime
from typing import Optional

from pydantic import BaseModel
from pydantic import EmailStr


class User(BaseModel):
    id: str
    firstname: str
    lastname: str
    birthday: datetime.date
    children: int
    phone: Optional[str] = None
    email: Optional[EmailStr] = None


class UserUpdate(BaseModel):
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    birthday: Optional[datetime.date] = None
    children: Optional[int] = None
    phone: Optional[str] = None
    email: Optional[EmailStr] = None
