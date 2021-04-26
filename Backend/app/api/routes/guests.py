# from app.core.config import db
from fastapi import APIRouter

router = APIRouter()
# users_repo = UsersRepository(db)


@router.get("/")
async def get_all():
    return {"key": "all"}


@router.get("/{id}")
async def get(id: int):
    return {"key": "single"}


@router.post("/")
async def create(id: int):
    return {"key": "create"}


@router.put("/{id}")
async def update(id: int):
    return {"key": "update"}


@router.delete("/{id}")
async def delete(id: int):
    return {"key": "delete"}
