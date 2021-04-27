from app.core.config import db
from app.db.repositories.receipt_items import ReceiptItemsRepository
from typing import List
from app.models.domain.receipt_items import (
    ReceiptItemOut,
    ReceiptItemInCreate,
    ReceiptItemInUpdate,
)
from fastapi import APIRouter

router = APIRouter()
repo = ReceiptItemsRepository(db)


@router.get("/", response_model=List[ReceiptItemOut])
async def get_all():
    model = await repo.get_all()
    return list(map(lambda m: ReceiptItemOut(**m), model))


@router.get("/{id}", response_model=ReceiptItemOut)
async def get(id: int):
    model = await repo.find_by_id(id)
    return ReceiptItemOut(**model)


@router.post("/", response_model=ReceiptItemOut)
async def create(receipt_item: ReceiptItemInCreate):
    model = await repo.create(receipt_item)
    return ReceiptItemOut(**model)


@router.put("/{id}", response_model=ReceiptItemOut)
async def update(id, receipt_item: ReceiptItemInUpdate):
    model = await repo.update(id, receipt_item)
    return ReceiptItemOut(**model)


@router.delete("/{id}")
async def delete(id: int):
    return await repo.delete(id)
