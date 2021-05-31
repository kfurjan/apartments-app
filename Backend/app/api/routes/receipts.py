from app.db.repositories.renters import RentersRepository
from app.db.repositories.guests import GuestsRepository
from app.core.config import db
from app.db.repositories.receipts import ReceiptsRepository
from typing import List
from app.models.domain.receipts import ReceiptOut, ReceiptInCreate, ReceiptInUpdate
from fastapi_jwt_auth import AuthJWT
from app.services.authorization import authorize_guest_or_renter, authorize_renter
from fastapi import APIRouter, Depends

router = APIRouter()
repo = ReceiptsRepository(db)
guests_repo = GuestsRepository(db)
renters_repo = RentersRepository(db)


@router.get("/", response_model=List[ReceiptOut])
async def get_all(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    email = Authorize.get_jwt_subject()
    user = await authorize_guest_or_renter(email)

    if user.role == "renter":
        renter = await renters_repo.get_renter_for_user(user.id)
        model = await repo.get_all_for_renter(renter.id)
        return list(map(lambda m: ReceiptOut(**m), model))
    else:
        guest = await guests_repo.get_guest_for_user(user.id)
        model = await repo.get_all_for_guest(guest.id)
        return list(map(lambda m: ReceiptOut(**m), model))


@router.get("/{id}", response_model=ReceiptOut)
async def get(id: int, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    email = Authorize.get_jwt_subject()
    user = await authorize_guest_or_renter(email)

    model = await repo.find_by_id(id)

    if user.role == "renter":
        renter = await renters_repo.get_renter_for_user(user.id)
        if model["renter_id"] == renter.id:
            return ReceiptOut(**model)
    else:
        guest = await guests_repo.get_guest_for_user(user.id)
        if model["guest_id"] == guest.id:
            return ReceiptOut(**model)


@router.post("/", response_model=ReceiptOut)
async def create(receipt: ReceiptInCreate, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    email = Authorize.get_jwt_subject()
    user = await authorize_renter(email)

    renter = await renters_repo.get_renter_for_user(user.id)

    receipt["renter_id"] = renter.id
    model = await repo.create(receipt)
    return ReceiptOut(**model)


@router.put("/{id}", response_model=ReceiptOut)
async def update(id: int, receipt: ReceiptInUpdate, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    email = Authorize.get_jwt_subject()
    user = await authorize_guest_or_renter(email)

    model = await repo.find_by_id(id)

    if user.role == "renter":
        renter = await renters_repo.get_renter_for_user(user.id)
        if model["renter_id"] == renter.id:
            receipt = await repo.update(id, model)
            return ReceiptOut(**receipt)
    else:
        guest = await guests_repo.get_guest_for_user(user.id)
        if model["guest_id"] == guest.id:
            receipt = await repo.update(id, model)
            return ReceiptOut(**receipt)
