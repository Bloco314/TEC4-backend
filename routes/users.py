from fastapi import APIRouter

from services.users import User

router = APIRouter()

@router.post("/users/")
async def create_user(email: str, senha: str, name: str):
    User.create_user(email, senha, name)
    return {"message": "User created successfully"}

@router.get("/users/{email}")
async def get_user(email: str):
    user = User.get_user(email)
    if user:
        return {"email": user[0], "senha": user[1], "name": user[2]}
    else:
        return {"message": "User not found"}

@router.get("/users/")
async def list_all_users():
    users = User.listall_user()
    return {"users": users}

@router.put("/users/{email}")
async def update_user(email: str, senha: str, name: str):
    User.update_user(email, senha, name)
    return {"message": "User updated successfully"}

@router.delete("/users/{email}")
async def delete_user(email: str):
    User.delete_user(email)
    return {"message": "User deleted successfully"}
