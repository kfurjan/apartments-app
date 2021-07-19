from app.core.config import db
from app.db.repositories.renters import RentersRepository
from app.models.domain.renters import RenterOut, RenterInCreate, RenterInUpdate
from fastapi_jwt_auth import AuthJWT
from app.services.authorization import authorize_renter
from fastapi import APIRouter, Depends

router = APIRouter()
repo = RentersRepository(db)


@router.get("/{id}", response_model=RenterOut)
async def get(id: int, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    email = Authorize.get_jwt_subject()
    user = await authorize_renter(email)

    model = await repo.find_by_id(id)
    if model and model.user_id == user.id:
        return RenterOut(**model)


@router.post("/", response_model=RenterOut)
async def create(renter: RenterInCreate, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    email = Authorize.get_jwt_subject()
    user = await authorize_renter(email)

    renter.user_id = user.id

    model = await repo.create(renter)
    return RenterOut(**model)


@router.put("/{id}", response_model=RenterOut)
async def update(id, renter: RenterInUpdate, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    email = Authorize.get_jwt_subject()
    user = await authorize_renter(email)

    old_renter = await repo.get_renter_for_user(user.id)
    if old_renter:
        model = await repo.update(id, renter)
        return RenterOut(**model)


@router.delete("/{id}")
async def delete(id: int, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    email = Authorize.get_jwt_subject()
    user = await authorize_renter(email)

    model = await repo.find_by_id(id)
    if model and model.user_id == user.id:
        return await repo.delete(id)
