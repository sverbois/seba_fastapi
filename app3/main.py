"""
Une petite application de type CRUD qui utilise une BD en RAM.
"""

from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import Response
from fastapi import status

from .db import USERS
from .schemas import User
from .schemas import UserUpdate

api = FastAPI()


@api.get("/")
def root():
    return {"message": "Une petite application de type CRUD"}


@api.get("/users")
def read_users():
    """Return all users"""
    return USERS


@api.get("/users/{user_id}")
def read_user(user_id: str):
    """Return a user"""
    if user_id not in USERS:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"L'utilisateur '{user_id}' n'est pas présent dans la base de données.",
        )
    return USERS[user_id]


@api.post("/users", status_code=status.HTTP_201_CREATED)
def create_user(user: User):
    """Add a new user"""
    user_id = user.id
    if user_id in USERS:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"L'utilisateur *{user_id}* est déjà présent dans la base de données.",
        )
    USERS[user_id] = user
    return user


@api.delete("/users/{user_id}")
def delete_user(user_id: str):
    """Delete a user"""
    if user_id in USERS:
        del USERS[user_id]
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@api.patch("/users/{user_id}")
def update_user(user_id: str, user: UserUpdate):
    """Update a user"""
    if user_id not in USERS:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"L'utilisateur *{user_id}* n'est pas présent dans la base de données.",
        )
    not_none_values = {k: v for k, v in user.dict().items() if v is not None}
    USERS[user_id].update(not_none_values)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
