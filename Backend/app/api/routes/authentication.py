from app.core.config import db
from app.db.errors import EntityDoesNotExist
from app.db.repositories.users import UsersRepository
from app.models.domain.users import User
from app.resources import strings
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from fastapi_jwt_auth import AuthJWT
from starlette.status import HTTP_400_BAD_REQUEST

router = APIRouter()
users_repo = UsersRepository(db)


@router.post("/login", response_model=User, name="authentication:login")
async def login(user: User, Authorize: AuthJWT = Depends()) -> User:
    try:
        await users_repo.get_user(user=user)
    except EntityDoesNotExist:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail=strings.INCORRECT_LOGIN_INPUT,
        )

    access_token = Authorize.create_access_token(subject=str(user.email))
    return JSONResponse({"access_token": access_token})
