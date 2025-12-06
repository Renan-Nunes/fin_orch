from fastapi import APIRouter, Depends
from controllers import UserController
from schemas.user_schema import UserResponse, UserCreate

router = APIRouter(prefix="/users", tags="user")

@router.post("/create", response=UserResponse)
async def create_user(dto: UserCreate, dbsession):
    response = await UserController.new_user(
        dto,
        dbsession
        )
    return response
