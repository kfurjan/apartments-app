# from app.core.config import db
from app.core.config import db
from app.db.repositories.apartment_details import ApartmentDetailsRepository
from typing import List
from app.models.domain.apartment_details import (
    ApartmentDetailOut,
    ApartmentDetailInCreate,
    ApartmentDetailInUpdate,
)
from fastapi import APIRouter

router = APIRouter()
repo = ApartmentDetailsRepository(db)


@router.get("/", response_model=List[ApartmentDetailOut])
async def get_all():
    models = await repo.get_all()
    return list(map(lambda m: ApartmentDetailOut(**m), models))


@router.get("/{id}", response_model=ApartmentDetailOut)
async def get(id: int):
    model = await repo.find_by_id(id)
    return ApartmentDetailOut(**model)


@router.post("/", response_model=ApartmentDetailOut)
async def create(apartment_detail: ApartmentDetailInCreate):
    model = await repo.create(apartment_detail)
    return ApartmentDetailOut(**model)


@router.put("/{id}", response_model=ApartmentDetailOut)
async def update(id, apartment_detail: ApartmentDetailInUpdate):
    model = await repo.update(id, apartment_detail)
    return ApartmentDetailOut(**model)


@router.delete("/{id}")
async def delete(id: int):
    return await repo.delete(id)
