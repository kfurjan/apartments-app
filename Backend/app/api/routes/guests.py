# from app.core.config import db
from app.db.repositories.users import UsersRepository
from app.core.config import db
from app.db.repositories.guests import GuestsRepository
from app.db.repositories.reservations import ReservationsRepository
from app.models.domain.guests import GuestOut, GuestInCreate, GuestInUpdate
from fastapi_jwt_auth import AuthJWT
from app.services.authorization import authorize_guest, authorize_renter
from fastapi import APIRouter, Depends

router = APIRouter()
repo = GuestsRepository(db)
user_repo = UsersRepository(db)
reservations_repo = ReservationsRepository(db)


@router.get("/{id}", response_model=GuestOut)
async def get(id: int, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    email = Authorize.get_jwt_subject()
    user = await authorize_guest(email)

    model = await repo.find_by_id(id)
    if model and model["user_id"] == user.id:
        return GuestOut(**model)


@router.post("/", response_model=GuestOut)
async def create(guest: GuestInCreate, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    email = Authorize.get_jwt_subject()
    user = await authorize_guest(email)

    guest.user_id = user.id

    model = await repo.create(guest)
    if model:
        return GuestOut(**model)


@router.put("/{id}", response_model=GuestOut)
async def update(id: int, guest: GuestInUpdate, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    email = Authorize.get_jwt_subject()
    user = await authorize_guest(email)

    old_guest = await repo.get_guest_for_user(user.id)
    if old_guest:
        model = await repo.update(id, guest)
        return GuestOut(**model)


@router.delete("/{id}")
async def delete(id: int, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    email = Authorize.get_jwt_subject()
    user = await authorize_guest(email)

    model = await repo.find_by_id(id)
    if model and model["user_id"] == user.id:
        return await repo.delete(id)


@router.get("/for_apartment")
async def for_apartment(apartment_id: int, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    email = Authorize.get_jwt_subject()
    await authorize_renter(email)

    models = await reservations_repo.guests_for_apartment(apartment_id)
    return list(map(lambda m: GuestOut(**m), models))
