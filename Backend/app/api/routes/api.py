from app.api.routes import users, authentication, guests
from fastapi import APIRouter

router = APIRouter()

router.include_router(users.router, tags=["users"], prefix="/user")
router.include_router(
    authentication.router, tags=["authentication"], prefix="/authentication"
)
router.include_router(guests.router, tags=["guests"], prefix="/guests")
