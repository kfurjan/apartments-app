from app.core.config import db
from app.db.repositories.users import UsersRepository
from app.models.domain.users import User
from app.resources import strings
from app.services.authentication import check_email_is_taken
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from fastapi_jwt_auth import AuthJWT
from starlette.status import HTTP_400_BAD_REQUEST

router = APIRouter()
users_repo = UsersRepository(db)


@router.get("", response_model=User, name="users:retrieve-user")
async def retrieve_user(Authorize: AuthJWT = Depends()) -> User:
    Authorize.jwt_required()
    current_user_email = Authorize.get_jwt_subject()
    user = await users_repo.get_user_by_email(email=current_user_email)

    return User(**user.dict())


@router.post("", response_model=User, name="users:create-user")
async def create_user(user: User, Authorize: AuthJWT = Depends()) -> JSONResponse:
    if await check_email_is_taken(users_repo, user.email):
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail=strings.EMAIL_TAKEN,
        )

    user = await users_repo.create_user(user=user)

    access_token = Authorize.create_access_token(subject=str(user.email))
    return JSONResponse({"access_token": access_token})
