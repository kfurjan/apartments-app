from app.core.config import db
from app.db.repositories.renters import RentersRepository
from typing import List
from app.models.domain.renters import RenterOut, RenterInCreate, RenterInUpdate
from fastapi import APIRouter

router = APIRouter()
repo = RentersRepository(db)


@router.get("/", response_model=List[RenterOut])
async def get_all():
    model = await repo.get_all()
    return list(map(lambda m: RenterOut(**m), model))


@router.get("/{id}", response_model=RenterOut)
async def get(id: int):
    model = await repo.find_by_id(id)
    return RenterOut(**model)


@router.post("/", response_model=RenterOut)
async def create(renter: RenterInCreate):
    model = await repo.create(renter)
    return RenterOut(**model)


@router.put("/{id}", response_model=RenterOut)
async def update(id, renter: RenterInUpdate):
    model = await repo.update(id, renter)
    return RenterOut(**model)


@router.delete("/{id}")
async def delete(id: int):
    return await repo.delete(id)
