import sqlite3
from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

from services.environments import Environment
from services.horarios import Horarios

router = APIRouter()


class Item(BaseModel):
    list: List[str]


@router.post("/env/create/")
def cria_ambiente(description, name: str, item: Item):
    try:
        Environment.create_environment(name, description)
        Horarios.createHorarios(item.list, name)
        return {"msg": "Created sucessfully!"}
    except sqlite3.IntegrityError:
        return {"msg": "PK-ERROR"}
    except sqlite3.OperationalError:
        return {"msg": "OP-ERROR"}


@router.get("/env/list/")
def lista_ambientes():
    envs = Environment.nameall_environment()

    if envs:
        return {"names": envs}


@router.get("/env/get/{name}")
def get_ambiente(name):
    try:
        nome, descricao = Environment.get_environment(name)
        horarios = Horarios.getHorarios(name)
        return {"nome": nome, "descricao": descricao, "horarios": horarios}
    except:
        return {"erro": "houve um erro"}


@router.post("/env/update/")
def edita_ambiente(description, name: str, item: Item):
    try:
        Environment.update_environment(name, description)
        Horarios.clearEnv(name)
        Horarios.createHorarios(item.list, name)
        return {"msg": "Updated sucessfully!"}
    except sqlite3.OperationalError:
        return {"msg": "OP-ERROR"}
