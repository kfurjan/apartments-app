from app.core.config import db
from app.db.repositories.locations import LocationsRepository
from typing import List
from app.models.domain.locations import LocationOut, LocationInCreate, LocationInUpdate
from fastapi_jwt_auth import AuthJWT
from app.services.authorization import authorize_renter
from fastapi import APIRouter, Depends

router = APIRouter()
repo = LocationsRepository(db)


@router.get("/", response_model=List[LocationOut])
async def get_all(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()

    model = await repo.get_all()
    return list(map(lambda m: LocationOut(**m), model))


@router.get("/{id}", response_model=LocationOut)
async def get(id: int, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()

    model = await repo.find_by_id(id)
    return LocationOut(**model)


@router.post("/", response_model=LocationOut)
async def create(location: LocationInCreate, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    email = Authorize.get_jwt_subject()
    await authorize_renter(email)

    model = await repo.create(location)
    return LocationOut(**model)


@router.put("/{id}", response_model=LocationOut)
async def update(id, location: LocationInUpdate, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    email = Authorize.get_jwt_subject()
    await authorize_renter(email)

    model = await repo.update(id, location)
    return LocationOut(**model)


@router.delete("/{id}")
async def delete(id: int, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    email = Authorize.get_jwt_subject()
    await authorize_renter(email)

    return await repo.delete(id)
