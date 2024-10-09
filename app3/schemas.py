import datetime

from pydantic import BaseModel
from pydantic import EmailStr


class User(BaseModel):
    id: str
    firstname: str
    lastname: str
    birthday: datetime.date
    children: int
    phone: str | None = None
    email: EmailStr | None = None


class UserUpdate(BaseModel):
    firstname: str | None = None
    lastname: str | None = None
    birthday: datetime.date | None = None
    children: int | None = None
    phone: str | None = None
    email: EmailStr | None = None
