from app.api.routes import (
    users,
    authentication,
    guests,
    apartments,
    renters,
    location_types,
    locations,
    ratings,
    receipt_items,
    receipts,
    reservations,
    services,
    apartment_details,
)
from fastapi import APIRouter

router = APIRouter()

router.include_router(
    authentication.router, tags=["authentication"], prefix="/authentication"
)
router.include_router(
    apartment_details.router, tags=["apartment_details"], prefix="/apartment_details"
)
router.include_router(users.router, tags=["users"], prefix="/user")
router.include_router(guests.router, tags=["guests"], prefix="/guests")
router.include_router(apartments.router, tags=["apartments"], prefix="/apartments")
router.include_router(renters.router, tags=["renters"], prefix="/renters")
router.include_router(
    location_types.router, tags=["location_types"], prefix="/location_types"
)
router.include_router(locations.router, tags=["locations"], prefix="/locations")
router.include_router(ratings.router, tags=["ratings"], prefix="/ratings")
router.include_router(
    receipt_items.router, tags=["receipt_items"], prefix="/receipt_items"
)
router.include_router(receipts.router, tags=["receipts"], prefix="/receipts")
router.include_router(
    reservations.router, tags=["reservations"], prefix="/reservations"
)
router.include_router(services.router, tags=["services"], prefix="/services")
