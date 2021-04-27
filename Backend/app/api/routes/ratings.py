from app.core.config import db
from app.db.repositories.ratings import RatingsRepository
from typing import List
from app.models.domain.ratings import RatingOut, RatingInCreate, RatingInUpdate
from fastapi import APIRouter

router = APIRouter()
repo = RatingsRepository(db)


@router.get("/", response_model=List[RatingOut])
async def get_all():
    model = await repo.get_all()
    return list(map(lambda m: RatingOut(**m), model))


@router.get("/{id}", response_model=RatingOut)
async def get(id: int):
    model = await repo.find_by_id(id)
    return RatingOut(**model)


@router.post("/", response_model=RatingOut)
async def create(rating: RatingInCreate):
    model = await repo.create(rating)
    return RatingOut(**model)


@router.put("/{id}", response_model=RatingOut)
async def update(id, rating: RatingInUpdate):
    model = await repo.update(id, rating)
    return RatingOut(**model)


@router.delete("/{id}")
async def delete(id: int):
    return await repo.delete(id)
