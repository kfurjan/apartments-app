from typing import List

from app.core.config import db
from app.db.repositories.apartments import ApartmentsRepository
from app.models.domain.apartments import (
    ApartmentInCreate,
    ApartmentInUpdate,
    ApartmentOut,
    ApartmentsQueryParams,
)
from fastapi import APIRouter, Request
from fastapi.params import Depends

router = APIRouter()
repo = ApartmentsRepository(db)


@router.get("/", response_model=List[ApartmentOut])
async def get_all(request: Request, _: ApartmentsQueryParams = Depends()):
    model = (
        await repo.get_all_filtered(ApartmentsQueryParams(**request.query_params))
        if dict(request.query_params)
        else await repo.get_all()
    )

    return list(map(lambda m: ApartmentOut(**m), model))


@router.get("/{id}", response_model=ApartmentOut)
async def get(id: int):
    model = await repo.find_by_id(id)
    return ApartmentOut(**model)


@router.post("/", response_model=ApartmentOut)
async def create(apartment: ApartmentInCreate):
    model = await repo.create(apartment)
    return ApartmentOut(**model)


@router.put("/{id}", response_model=ApartmentOut)
async def update(id, apartment: ApartmentInUpdate):
    model = await repo.update(id, apartment)
    return ApartmentOut(**model)


@router.delete("/{id}")
async def delete(id: int):
    return await repo.delete(id)
