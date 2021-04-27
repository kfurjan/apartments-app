from app.core.config import db
from app.db.repositories.reservations import ReservationsRepository
from typing import List
from app.models.domain.reservations import ReservationOut, ReservationInCreate, ReservationInUpdate
from fastapi import APIRouter

router = APIRouter()
repo = ReservationsRepository(db)


@router.get("/", response_model=List[ReservationOut])
async def get_all():
    model = await repo.get_all()
    return list(map(lambda m: ReservationOut(**m), model))


@router.get("/{id}", response_model=ReservationOut)
async def get(id: int):
    model = await repo.find_by_id(id)
    return ReservationOut(**model)


@router.post("/", response_model=ReservationOut)
async def create(reservation: ReservationInCreate):
    model = await repo.create(reservation)
    return ReservationOut(**model)


@router.put("/{id}", response_model=ReservationOut)
async def update(id, reservation: ReservationInUpdate):
    model = await repo.update(id, reservation)
    return ReservationOut(**model)


@router.delete("/{id}")
async def delete(id: int):
    return await repo.delete(id)
