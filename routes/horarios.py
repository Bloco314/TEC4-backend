from fastapi import APIRouter
from services.horarios import Horarios

router = APIRouter()


@router.get("/hour/")
async def get_horario(env_name: str):
    lista = Horarios.getHorarios(env_name)
    return {"horarios": lista}
