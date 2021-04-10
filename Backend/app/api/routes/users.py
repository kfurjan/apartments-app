from app.api.dependencies.database import get_repository
from app.db.repositories.users import UsersRepository
from app.models.domain.users import User
from fastapi import APIRouter, Depends
from pydantic import EmailStr

router = APIRouter()


@router.get("", response_model=User, name="users:retrieve-user")
async def retrieve_user(
    email: EmailStr,
    users_repo: UsersRepository = Depends(get_repository(UsersRepository)),
) -> User:
    user = await users_repo.get_user_by_email(email=email)

    return User(email=user.email, password=user.password)


@router.put("", response_model=User, name="users:create-user")
async def create_user(
    user: User,
    users_repo: UsersRepository = Depends(get_repository(UsersRepository)),
) -> User:
    user = await users_repo.create_user(email=user.email, password=user.password)

    return User(email=user.email, password=user.password)
