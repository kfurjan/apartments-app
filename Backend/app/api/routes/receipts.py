from app.core.config import db
from app.db.repositories.receipts import ReceiptsRepository
from typing import List
from app.models.domain.receipts import ReceiptOut, ReceiptInCreate, ReceiptInUpdate
from fastapi import APIRouter

router = APIRouter()
repo = ReceiptsRepository(db)


@router.get("/", response_model=List[ReceiptOut])
async def get_all():
    model = await repo.get_all()
    return list(map(lambda m: ReceiptOut(**m), model))


@router.get("/{id}", response_model=ReceiptOut)
async def get(id: int):
    model = await repo.find_by_id(id)
    return ReceiptOut(**model)


@router.post("/", response_model=ReceiptOut)
async def create(receipt: ReceiptInCreate):
    model = await repo.create(receipt)
    return ReceiptOut(**model)


@router.put("/{id}", response_model=ReceiptOut)
async def update(id, receipt: ReceiptInUpdate):
    model = await repo.update(id, receipt)
    return ReceiptOut(**model)


@router.delete("/{id}")
async def delete(id: int):
    return await repo.delete(id)
