from fastapi import APIRouter

from api.users import views as user


api = APIRouter()

api.include_router(user.router, prefix="/user", tags=["User"])