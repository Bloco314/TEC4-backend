from fastapi import APIRouter

from services.users import User

router = APIRouter()

@router.get("/users/all")
async def all_users():
    return User.listall_user()