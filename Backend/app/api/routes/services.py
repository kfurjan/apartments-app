from app.core.config import db
from app.db.repositories.services import ServicesRepository
from typing import List
from app.models.domain.services import ServiceOut, ServiceInCreate, ServiceInUpdate
from app.db.repositories.renters import RentersRepository
from fastapi_jwt_auth import AuthJWT
from app.services.authorization import authorize_renter
from fastapi import APIRouter, Depends

router = APIRouter()
repo = ServicesRepository(db)


@router.get("/", response_model=List[ServiceOut])
async def get_all(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    email = Authorize.get_jwt_subject()
    await authorize_renter(email)

    model = await repo.get_all()
    return list(map(lambda m: ServiceOut(**m), model))


@router.get("/{id}", response_model=ServiceOut)
async def get(id: int, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    email = Authorize.get_jwt_subject()
    await authorize_renter(email)

    model = await repo.find_by_id(id)
    return ServiceOut(**model)


@router.post("/", response_model=ServiceOut)
async def create(service: ServiceInCreate, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    email = Authorize.get_jwt_subject()
    await authorize_renter(email)

    model = await repo.create(service)
    return ServiceOut(**model)


@router.put("/{id}", response_model=ServiceOut)
async def update(id, service: ServiceInUpdate, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    email = Authorize.get_jwt_subject()
    await authorize_renter(email)

    model = await repo.update(id, service)
    return ServiceOut(**model)


@router.delete("/{id}")
async def delete(id: int, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    email = Authorize.get_jwt_subject()
    await authorize_renter(email)

    return await repo.delete(id)
