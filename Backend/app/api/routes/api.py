from app.api.routes import users
from fastapi import APIRouter

router = APIRouter()

router.include_router(users.router, tags=["users"], prefix="/user")
