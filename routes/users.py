from fastapi import APIRouter

from services.users import User

router = APIRouter()

@router.post("/users/")
async def create_user(email: str, senha: str, name: str,tipo: str):
    User.create_user(email, senha, name, tipo)
    return {"message": "User created successfully"}

@router.get("/users/login/{email}/{senha}")
async def login(email,senha):
    user = User.login(email,senha)

    if user:
        return {"name":user[2],"tipo":user[3]}
    
@router.get("/users/list_colaborator/")
async def list_colaborators():
    users = User.list_colaborators()

    if users:
        return {"colaborators":users}

@router.put("/users/{email}")
async def update_user(email: str, senha: str, name: str):
    User.update_user(email, senha, name)
    return {"message": "User updated successfully"}

@router.delete("/users/{email}")
async def delete_user(email: str):
    User.delete_user(email)
    return {"message": "User deleted successfully"}
