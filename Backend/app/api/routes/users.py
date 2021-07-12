from app.core.config import db
from app.db.repositories.users import UsersRepository
from app.models.domain.users import UserOutDetails, UserInCreate
from app.db.repositories.guests import GuestsRepository
from app.db.repositories.renters import RentersRepository
from app.resources import strings
from app.services.authentication import (
    check_email_is_taken,
    get_password_hash,
)
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from fastapi_jwt_auth import AuthJWT
from starlette.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

router = APIRouter()
users_repo = UsersRepository(db)
guests_repo = GuestsRepository(db)
renters_repo = RentersRepository(db)


@router.get("", name="users:retrieve-user")
async def retrieve_user(Authorize: AuthJWT = Depends()) -> UserOutDetails:
    Authorize.jwt_required()
    current_user_email = Authorize.get_jwt_subject()
    user = await users_repo.get_user_by_email(email=current_user_email)

    if user.role == "renter":
        renter = await renters_repo.get_renter_for_user(user.id)
        user.renter_id = renter.id if renter is not None else None
    else:
        guest = await guests_repo.get_guest_for_user(user.id)
        user.guest_id = guest.id if guest is not None else None

    return UserOutDetails(**user.dict())


@router.post(
    "",
    status_code=HTTP_201_CREATED,
    name="users:create-user",
)
async def create_user(
    user: UserInCreate, Authorize: AuthJWT = Depends()
) -> JSONResponse:
    if await check_email_is_taken(users_repo, user.email):
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail=strings.EMAIL_TAKEN,
        )

    user.password_digest = get_password_hash(user.password_digest)
    user = await users_repo.create_user(user=UserInCreate(**user.dict()))

    access_token = Authorize.create_access_token(subject=str(user.email))
    return JSONResponse({"access_token": access_token})
