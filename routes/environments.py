import sqlite3
from fastapi import APIRouter

from services.environments import Environment

router = APIRouter()

@router.post('/env/create/')
def cria_ambiente(description,name: str):
    try:
        Environment.create_environment(name,description)
        return {"msg":"Created sucessfully!"}
    except sqlite3.IntegrityError:
        return {"msg":"PK-ERROR"}
    except sqlite3.OperationalError:
        return {"msg":"OP-ERROR"}
   

@router.get('/env/list/')
def lista_ambientes():
    envs = Environment.nameall_environment()

    if envs:
        return {'names':envs}