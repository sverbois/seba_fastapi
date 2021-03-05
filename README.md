# SEBA FastAPI

Quelques petites applications pour accompagner une introduction au framework *FastAPI*.

## Installation

    git clone https://github.com/sverbois/seba_fastapi.git
    cd seba_fastapi
    python3.8 -m venv venv
    ./venv/bin/pip install --upgrade pip
    ./venv/bin/pip install -r requirements.txt

## Applications

### Use query, path, headers and body parameters

    ./venv/bin/uvicorn app1.main:api --reload

### *Add to 42* application

    ./venv/bin/uvicorn app2.main:api --reload

### A simple CRUD application

    ./venv/bin/uvicorn app3.main:api --reload