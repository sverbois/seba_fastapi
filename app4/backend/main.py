import csv
import pathlib
from typing import Annotated

from fastapi import Body
from fastapi import FastAPI
from fastapi import status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pydantic import EmailStr

DATA_FILE = str(pathlib.Path(__file__).parent.joinpath("registrations.csv"))


class Registration(BaseModel):
    firstname: str
    lastname: str
    email: EmailStr


api = FastAPI()

api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@api.get("/")
def root():
    return {"message": "Registration application home"}


@api.post("/registrations", status_code=status.HTTP_201_CREATED)
def create_registration(
    data: Annotated[Registration, Body(description="Registration data")],
):
    append_data_in_csv_file(data.model_dump())
    return {"message": "Inscription enregistrée"}


def append_data_in_csv_file(data: dict):
    with open(DATA_FILE, "a", newline="") as f:
        fieldnames = list(Registration.model_json_schema()["properties"].keys())
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow(data)
