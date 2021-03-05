import datetime
from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    id: str
    firstname: str
    lastname: str
    birthday: datetime.date
    children: int


class UserUpdate(BaseModel):
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    birthday: Optional[datetime.date] = None
    children: Optional[int] = None
