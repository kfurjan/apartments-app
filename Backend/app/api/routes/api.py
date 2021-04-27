from app.api.routes import users, authentication, guests
from fastapi import APIRouter

router = APIRouter()

router.include_router(
    authentication.router, tags=["authentication"], prefix="/authentication"
)
router.include_router(
    guests.router, tags=["apartment_details"], prefix="/apartment_details"
)

router.include_router(users.router, tags=["users"], prefix="/user")
router.include_router(guests.router, tags=["guests"], prefix="/guests")
router.include_router(guests.router, tags=["apartments"], prefix="/apartments")
router.include_router(guests.router, tags=["location_types"], prefix="/location_types")
router.include_router(guests.router, tags=["locations"], prefix="/locations")
router.include_router(guests.router, tags=["ratings"], prefix="/ratings")
router.include_router(guests.router, tags=["receipt_items"], prefix="/receipt_items")
router.include_router(guests.router, tags=["receipts"], prefix="/receipts")
router.include_router(guests.router, tags=["reservations"], prefix="/reservations")
router.include_router(guests.router, tags=["services"], prefix="/services")
