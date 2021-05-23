from app.db.repositories.renters import RentersRepository
from app.db.repositories.apartments import ApartmentsRepository
from app.core.config import db
from app.db.repositories.apartment_details import ApartmentDetailsRepository
from typing import List
from app.models.domain.apartment_details import (
    ApartmentDetailOut,
    ApartmentDetailInCreate,
    ApartmentDetailInUpdate,
)
from fastapi_jwt_auth import AuthJWT
from app.services.authorization import authorize_renter
from fastapi import APIRouter, Depends

router = APIRouter()
repo = ApartmentDetailsRepository(db)
apartment_repo = ApartmentsRepository(db)
renters_repo = RentersRepository(db)


@router.get("/", response_model=List[ApartmentDetailOut])
async def get_all(apartment_id: int):
    models = await repo.get_all_for_apartment(apartment_id)
    return list(map(lambda m: ApartmentDetailOut(**m), models))


@router.get("/{id}", response_model=ApartmentDetailOut)
async def get(id: int):
    model = await repo.find_by_id(id)
    return ApartmentDetailOut(**model)


@router.post("/", response_model=ApartmentDetailOut)
async def create(
    apartment_detail: ApartmentDetailInCreate, Authorize: AuthJWT = Depends()
):
    Authorize.jwt_required()
    email = Authorize.get_jwt_subject()
    user = await authorize_renter(email)

    renter = await renters_repo.get_renter_for_user(user.id)
    apartment = await apartment_repo.find_by_id(apartment_detail.apartment_id)

    if apartment.renter_id == renter.id:
        model = await repo.create(apartment_detail)
        return ApartmentDetailOut(**model)


@router.put("/{id}", response_model=ApartmentDetailOut)
async def update(
    id, apartment_detail: ApartmentDetailInUpdate, Authorize: AuthJWT = Depends()
):
    Authorize.jwt_required()
    email = Authorize.get_jwt_subject()
    user = await authorize_renter(email)

    renter = await renters_repo.get_renter_for_user(user.id)
    apartment = await apartment_repo.find_by_id(apartment_detail.apartment_id)

    if apartment.renter_id == renter.id:
        model = await repo.update(id, apartment_detail)
        return ApartmentDetailOut(**model)


@router.delete("/{id}")
async def delete(id: int, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    email = Authorize.get_jwt_subject()
    user = await authorize_renter(email)

    renter = await renters_repo.get_renter_for_user(user.id)
    apartment_detail = await repo.find_by_id(id)
    apartment = await apartment_repo.find_by_id(apartment_detail.apartment_id)

    if apartment.renter_id == renter.id:
        return await repo.delete(id)
