from fastapi import APIRouter, Depends, HTTPException

from app.auth.auth_utils import get_current_active_user, get_password_hash
from app.database import db
from app.models.user import User, UserInDB

router = APIRouter()


@router.get("/users/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user


@router.get("/users/me/items")
async def read_own_items(current_user: User = Depends(get_current_active_user)):
    return [{"item_id": 1, "owner": current_user}]


@router.post("/user/create")
async def create_user(
    username: str, password: str, email: str = None, full_name: str = None
):
    hashed_password = get_password_hash(password)
    user_data = {
        "username": username,
        "email": email,
        "full_name": full_name,
        "hashed_password": hashed_password,
        "disabled": False,
    }
    await db["users"].insert_one(user_data)
    return {"msg": "User created successfully"}
