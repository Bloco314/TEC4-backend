import sqlite3
from fastapi import APIRouter
from services.equipments import Equipment


router = APIRouter()


@router.post("/equip/create/")
def cria_equipamento(name: str, description: str, env: str, tag: str):
    try:
        Equipment.create_equipment(name, description, env, tag)
    except sqlite3.IntegrityError:
        return {"msg": "PK-ERROR"}
    except sqlite3.OperationalError:
        return {"msg": "OP-ERROR"}


@router.get("/equips/list/")
def lista_equipamentos():
    equips = Equipment.listall_equipment()
    return {"equips": equips}


@router.get("/equip/get/{name}")
def get_equipamento(name: str):
    try:
        equip = Equipment.get_equipment(name)
    except:
        return {"erro": "houve um erro"}


@router.post("/equip/update/")
def edita_ambiente(name: str, description: str, env: str, tag: str):
    try:
        Equipment.update_equipment(name, description, tag, env_name=env)
        return {"msg": "Updated sucessfully!"}
    except sqlite3.OperationalError:
        return {"msg": "OP-ERROR"}


@router.delete("/equip/delete/{name}")
def deleta_ambiente(name):
    try:
        Equipment.delete_equipment(name)
        return {"msg": "Updated sucessfully!"}
    except sqlite3.OperationalError:
        return {"msg": "OP-ERROR"}
