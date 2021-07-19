from datetime import timedelta
from app.db.repositories.renters import RentersRepository
from app.core.config import db
from app.db.repositories.apartments import ApartmentsRepository
from typing import List
from app.models.domain.apartments import (
    ApartmentInCreate,
    ApartmentInUpdate,
    ApartmentOut,
    ApartmentsQueryParams,
)
from fastapi import APIRouter, Request
from fastapi.params import Depends
from fastapi_jwt_auth import AuthJWT
from app.services.authorization import authorize_renter

router = APIRouter()
repo = ApartmentsRepository(db)
renters_repo = RentersRepository(db)


@router.get("/", response_model=List[ApartmentOut])
async def get_all(request: Request, _: ApartmentsQueryParams = Depends()):
    model = (
        await repo.get_all_filtered(ApartmentsQueryParams(**request.query_params))
        if dict(request.query_params)
        else await repo.get_all()
    )

    return list(map(lambda m: ApartmentOut(**m), model))


@router.get("/{id}", response_model=ApartmentOut)
async def get(id: int):
    model = await repo.find_by_id(id)
    return ApartmentOut(**model)


@router.get("/{id}/unavailable_dates", response_model=List[str])
async def unavailable_dates(id: int):
    dates = await repo.get_unavailable_dates(id)
    all_dates = map(
        lambda m: [
            m["starts_at"] + timedelta(days=x)
            for x in range((m["ends_at"] - m["starts_at"]).days + 1)
        ],
        dates,
    )
    strings = map(lambda m: m.strftime("%Y-%m-%d"), sum(all_dates, []))
    return list(dict.fromkeys(strings))


@router.post("/", response_model=ApartmentOut)
async def create(apartment: ApartmentInCreate, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    email = Authorize.get_jwt_subject()
    user = await authorize_renter(email)
    renter = await renters_repo.get_renter_for_user(user.id)

    apartment.renter_id = renter.id
    model = await repo.create(apartment)
    return ApartmentOut(**model)


@router.put("/{id}", response_model=ApartmentOut)
async def update(id, apartment: ApartmentInUpdate, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    email = Authorize.get_jwt_subject()
    user = await authorize_renter(email)
    renter = renters_repo.get_renter_for_user(user.id)

    if renter.id == apartment.renter_id:
        model = await repo.update(id, apartment)
        return ApartmentOut(**model)


@router.delete("/{id}")
async def delete(id: int, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    email = Authorize.get_jwt_subject()
    user = await authorize_renter(email)
    renter = renters_repo.get_renter_for_user(user.id)

    model = await repo.find_by_id(id)
    if model and renter.id == model["renter_id"]:
        return await repo.delete(id)
