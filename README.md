# seba_fastapi

Quelques petites applications *FastAPI* pour accompagner une introduction au framework.

## Installation

    git clone https://github.com/sverbois/seba_fastapi.git
    cd seba_fastapi
    python3.8 -m venv venv
    ./venv/bin/pip install --upgrade pip
    ./venv/bin/pip install -r requirements.txt

## Démarrer une application

    cd seba_fastapi
    ./venv/bin/uvicorn app1.main:api --reload
