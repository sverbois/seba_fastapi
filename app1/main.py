from typing import Annotated

from fastapi import Body
from fastapi import FastAPI
from fastapi import Header
from fastapi import Path
from fastapi import Query

api = FastAPI()


@api.get("/")
def root():
    return {"message": "Hello World !!!"}


@api.get("/hello")
def hello(
    name: Annotated[str, Query()],  # ou name: str
):
    message = f"Hello {name} !!!"
    return {"message": message}


@api.get("/hello-optional")
def hello_optional(
    name: Annotated[str | None, Query()] = None,
):
    if name is None:
        name = "stranger"
    message = f"Hello {name} !!!"
    return {"message": message}


@api.get("/items/{item_id}")
def read_item(
    item_id: Annotated[int, Path()],  # ou item_id: int
):
    return {"item_id": item_id}


@api.get("/headers")
def get_user_agent(
    user_agent: Annotated[str, Header()],
):
    return {"User-Agent": user_agent}


@api.post("/items")
def create_item(
    item: Annotated[dict, Body()],  # ou item: dict
):
    return {"item": item}


@api.post("/all/{item_id}")
def return_all_parameters(
    item_id: Annotated[int, Path()],
    user_agent: Annotated[str, Header()],
    item: Annotated[dict, Body()],
    name: Annotated[str, Query()],
):
    return {"name": name, "item_id": item_id, "user_agent": user_agent, "item": item}
