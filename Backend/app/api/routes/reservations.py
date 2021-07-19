from app.core.config import db
from app.db.repositories.reservations import ReservationsRepository
from app.db.repositories.guests import GuestsRepository
from app.db.repositories.renters import RentersRepository
from typing import List
from app.models.domain.reservations import (
    ReservationOut,
    ReservationInCreate,
    ReservationInUpdate,
)
from fastapi_jwt_auth import AuthJWT
from app.services.authorization import authorize_guest_or_renter, authorize_guest
from fastapi import APIRouter, Depends

router = APIRouter()
repo = ReservationsRepository(db)
guests_repo = GuestsRepository(db)
renters_repo = RentersRepository(db)


@router.get("/", response_model=List[ReservationOut])
async def get_all(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    email = Authorize.get_jwt_subject()
    user = await authorize_guest_or_renter(email)

    if user.role == "renter":
        renter = renters_repo.get_renter_for_user(user.id)
        model = await repo.get_all_for_renter(renter.id)
        return list(map(lambda m: ReservationOut(**m), model))
    else:
        guest = guests_repo.get_guest_for_user(user.id)
        model = await repo.get_all_for_guest(guest.id)
        return list(map(lambda m: ReservationOut(**m), model))


@router.get("/{id}", response_model=ReservationOut)
async def get(id: int, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    email = Authorize.get_jwt_subject()
    user = await authorize_guest_or_renter(email)

    model = await repo.find_by_id(id)

    if user.role == "renter":
        renter = renters_repo.get_renter_for_user(user.id)
        if model["renter_id"] == renter.id:
            return ReservationOut(**model)
    else:
        guest = guests_repo.get_guest_for_user(user.id)
        if model["guest_id"] == guest.id:
            return ReservationOut(**model)


@router.post("/", response_model=ReservationOut)
async def create(reservation: ReservationInCreate, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    email = Authorize.get_jwt_subject()
    await authorize_guest(email)

    model = await repo.create(reservation)
    return ReservationOut(**model)


@router.put("/{id}", response_model=ReservationOut)
async def update(
    id: int, reservation: ReservationInUpdate, Authorize: AuthJWT = Depends()
):
    Authorize.jwt_required()
    email = Authorize.get_jwt_subject()
    user = await authorize_guest_or_renter(email)

    model = await repo.find_by_id(id)

    if user.role == "renter":
        renter = renters_repo.get_renter_for_user(user.id)
        if model["renter_id"] == renter.id:
            reservation = await repo.update(id, model)
            return ReservationOut(**reservation)
    else:
        guest = guests_repo.get_guest_for_user(user.id)
        if model["guest_id"] == guest.id:
            reservation = await repo.update(id, model)
            return ReservationOut(**reservation)


@router.delete("/{id}")
async def delete(id: int, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    email = Authorize.get_jwt_subject()
    user = await authorize_guest_or_renter(email)

    model = await repo.find_by_id(id)

    if user.role == "renter":
        renter = renters_repo.get_renter_for_user(user.id)
        if model["renter_id"] == renter.id:
            return await repo.delete(id)
    else:
        guest = guests_repo.get_guest_for_user(user.id)
        if model["guest_id"] == guest.id:
            return await repo.delete(id)
