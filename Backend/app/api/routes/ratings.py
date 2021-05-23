from app.core.config import db
from app.db.repositories.ratings import RatingsRepository
from typing import List
from app.models.domain.ratings import RatingOut, RatingInCreate, RatingInUpdate
from fastapi_jwt_auth import AuthJWT
from app.services.authorization import authorize_guest, authorize_renter
from fastapi import APIRouter, Depends

router = APIRouter()
repo = RatingsRepository(db)


@router.get("/", response_model=List[RatingOut])
async def get_all(apartment_id: int, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    email = Authorize.get_jwt_subject()
    await authorize_guest(email)

    models = await repo.get_all_for_apartment(apartment_id)
    return list(map(lambda m: RatingOut(**m), models))


@router.post("/", response_model=RatingOut)
async def create(rating: RatingInCreate, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    email = Authorize.get_jwt_subject()
    await authorize_guest(email)

    model = await repo.create(rating)
    return RatingOut(**model)


@router.put("/{id}", response_model=RatingOut)
async def update(id, rating: RatingInUpdate, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    email = Authorize.get_jwt_subject()
    await authorize_guest(email)

    model = await repo.update(id, rating)
    return RatingOut(**model)
