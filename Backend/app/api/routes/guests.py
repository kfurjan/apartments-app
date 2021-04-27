# from app.core.config import db
from app.core.config import db
from app.db.repositories.guests import GuestsRepository
from typing import List
from app.models.domain.guests import GuestOut, GuestInCreate, GuestInUpdate
from fastapi import APIRouter

router = APIRouter()
repo = GuestsRepository(db)


@router.get("/", response_model=List[GuestOut])
async def get_all():
    orm_models = await repo.get_all()
    return list(map(lambda m: GuestOut(**m), orm_models))


@router.get("/{id}", response_model=GuestOut)
async def get(id: int):
    orm_model = await repo.find_by_id(id)
    return GuestOut(**orm_model)


@router.post("/", response_model=GuestOut)
async def create(guest: GuestInCreate):
    orm_model = await repo.create(guest)
    return GuestOut(**orm_model)


@router.put("/{id}", response_model=GuestOut)
async def update(id, guest: GuestInUpdate):
    orm_model = await repo.update(id, guest)
    return GuestOut(**orm_model)


@router.delete("/{id}")
async def delete(id: int):
    return await repo.delete(id)
