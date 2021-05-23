from app.core.config import db
from app.db.repositories.location_types import LocationTypesRepository
from typing import List
from app.models.domain.location_types import (
    LocationTypeOut,
    LocationTypeInCreate,
    LocationTypeInUpdate,
)
from fastapi import APIRouter

router = APIRouter()
repo = LocationTypesRepository(db)


@router.get("/", response_model=List[LocationTypeOut])
async def get_all():
    model = await repo.get_all()
    return list(map(lambda m: LocationTypeOut(**m), model))


@router.get("/{id}", response_model=LocationTypeOut)
async def get(id: int):
    model = await repo.find_by_id(id)
    return LocationTypeOut(**model)


# @router.post("/", response_model=LocationTypeOut)
# async def create(location_type: LocationTypeInCreate):
#     model = await repo.create(location_type)
#     return LocationTypeOut(**model)


# @router.put("/{id}", response_model=LocationTypeOut)
# async def update(id, location_type: LocationTypeInUpdate):
#     model = await repo.update(id, location_type)
#     return LocationTypeOut(**model)


# @router.delete("/{id}")
# async def delete(id: int):
#     return await repo.delete(id)
