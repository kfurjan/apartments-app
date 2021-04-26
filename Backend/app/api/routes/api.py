from app.api.routes import users, authentication
from fastapi import APIRouter

router = APIRouter()

router.include_router(users.router, tags=["users"], prefix="/user")
router.include_router(
    authentication.router, tags=["authentication"], prefix="/authentication"
)
