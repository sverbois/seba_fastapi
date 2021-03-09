from typing import Optional

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
def hello(name: str = Query(...)):
    # def hello(name: str):
    # def hello(name):
    message = f"Hello {name} !!!"
    return {"message": message}


@api.get("/hello-optional")
def hello_optional(name: str = Query(None)):
    # def hello(name: Optional(str) = None):
    if name is None:
        name = "stranger"
    message = f"Hello {name} !!!"
    return {"message": message}


@api.get("/items/{item_id}")
def read_item(item_id: str = Path(...)):
    # def read_item(item_id: str):
    # def read_item(item_id):
    return {"item_id": item_id}


@api.get("/headers")
def get_user_agent(user_agent: str = Header(...)):
    return {"User-Agent": user_agent}


@api.post("/items")
def create_item(item: dict = Body(...)):
    # def create_item(item: dict):
    return {"item": item}
