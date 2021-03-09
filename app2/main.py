from fastapi import FastAPI
from pydantic import BaseModel

api = FastAPI()


@api.get("/add-to-42")
def add_to_42_query(number: int):
    return 42 + number


@api.get("/add-to-42/{number}")
def add_to_42_path(number: int):
    return 42 + number


class BodyModel(BaseModel):
    number1: int
    number2: int = 0


@api.post("/add-to-42")
def add_to_42_body(body: BodyModel):
    return 42 + body.number1 + body.number2
