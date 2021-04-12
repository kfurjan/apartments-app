from app.core.config import db
from app.db.repositories.users import UsersRepository
from app.models.domain.users import User
from fastapi import APIRouter
from pydantic import EmailStr

router = APIRouter()
users_repo = UsersRepository(db)


@router.get("", response_model=User, name="users:retrieve-user")
async def retrieve_user(email: EmailStr) -> User:
    user = await users_repo.get_user_by_email(email=email)

    return User(**user.dict())


@router.put("", response_model=User, name="users:create-user")
async def create_user(user: User) -> User:
    user = await users_repo.create_user(user=user)

    return User(**user.dict())
