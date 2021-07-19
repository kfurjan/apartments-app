from app.core.config import db
from app.db.repositories.receipt_items import ReceiptItemsRepository
from typing import List
from app.models.domain.receipt_items import (
    ReceiptItemOut,
    ReceiptItemInCreate,
    ReceiptItemInUpdate,
)
from fastapi_jwt_auth import AuthJWT
from app.services.authorization import authorize_renter
from fastapi import APIRouter, Depends

router = APIRouter()
repo = ReceiptItemsRepository(db)


@router.get("/", response_model=List[ReceiptItemOut])
async def get_all(receipt_id: int, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()

    if receipt_id:
        model = await repo.get_all_for_receipt(receipt_id)
        return list(map(lambda m: ReceiptItemOut(**m), model))


@router.get("/{id}", response_model=ReceiptItemOut)
async def get(id: int, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    model = await repo.find_by_id(id)
    return ReceiptItemOut(**model)


@router.post("/", response_model=ReceiptItemOut)
async def create(receipt_item: ReceiptItemInCreate, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    email = Authorize.get_jwt_subject()
    await authorize_renter(email)

    model = await repo.create(receipt_item)
    return ReceiptItemOut(**model)


@router.put("/{id}", response_model=ReceiptItemOut)
async def update(
    id: int, receipt_item: ReceiptItemInUpdate, Authorize: AuthJWT = Depends()
):
    Authorize.jwt_required()
    email = Authorize.get_jwt_subject()
    await authorize_renter(email)

    model = await repo.update(id, receipt_item)
    return ReceiptItemOut(**model)


@router.delete("/{id}")
async def delete(id: int, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    email = Authorize.get_jwt_subject()
    await authorize_renter(email)

    return await repo.delete(id)
