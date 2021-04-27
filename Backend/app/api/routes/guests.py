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
    models = await repo.get_all()
    return list(map(lambda m: GuestOut(**m), models))


@router.get("/{id}", response_model=GuestOut)
async def get(id: int):
    model = await repo.find_by_id(id)
    return GuestOut(**model)


@router.post("/", response_model=GuestOut)
async def create(guest: GuestInCreate):
    model = await repo.create(guest)
    return GuestOut(**model)


@router.put("/{id}", response_model=GuestOut)
async def update(id, guest: GuestInUpdate):
    model = await repo.update(id, guest)
    return GuestOut(**model)


@router.delete("/{id}")
async def delete(id: int):
    return await repo.delete(id)
