from app.core.config import db
from app.db.repositories.services import ServicesRepository
from typing import List
from app.models.domain.services import ServiceOut, ServiceInCreate, ServiceInUpdate
from fastapi import APIRouter

router = APIRouter()
repo = ServicesRepository(db)


@router.get("/", response_model=List[ServiceOut])
async def get_all():
    model = await repo.get_all()
    return list(map(lambda m: ServiceOut(**m), model))


@router.get("/{id}", response_model=ServiceOut)
async def get(id: int):
    model = await repo.find_by_id(id)
    return ServiceOut(**model)


@router.post("/", response_model=ServiceOut)
async def create(service: ServiceInCreate):
    model = await repo.create(service)
    return ServiceOut(**model)


@router.put("/{id}", response_model=ServiceOut)
async def update(id, service: ServiceInUpdate):
    model = await repo.update(id, service)
    return ServiceOut(**model)


@router.delete("/{id}")
async def delete(id: int):
    return await repo.delete(id)
