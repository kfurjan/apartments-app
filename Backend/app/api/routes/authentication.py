from app.core.config import db, jwt_token_denylist
from app.db.errors import EntityDoesNotExist
from app.db.repositories.users import UsersRepository
from app.models.domain.users import User
from app.resources import strings
from app.services.authentication import verify_password
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from fastapi_jwt_auth import AuthJWT
from starlette.status import HTTP_400_BAD_REQUEST

router = APIRouter()
users_repo = UsersRepository(db)


@router.post("/login", name="authentication:login")
async def login(user: User, Authorize: AuthJWT = Depends()) -> JSONResponse:
    try:
        user_in_db = await users_repo.get_user(user=user)
    except EntityDoesNotExist:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail=strings.INCORRECT_LOGIN_INPUT,
        )

    if not verify_password(user.password_digest, user_in_db.password_digest):
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail=strings.INCORRECT_PASSWORD,
        )

    access_token = Authorize.create_access_token(subject=str(user.email))
    return JSONResponse({"access_token": access_token})


@router.post("/logout", name="authentication:logout")
async def logout(Authorize: AuthJWT = Depends()) -> JSONResponse:
    Authorize.jwt_required()
    jwt_token_denylist.add(Authorize.get_raw_jwt()["jti"])

    return JSONResponse({"detail": "Access token has been revoked"})
