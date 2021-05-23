from app.db.repositories.users import UsersRepository
from app.db.repositories.renters import RentersRepository
from app.db.repositories.guests import GuestsRepository
from fastapi.exceptions import HTTPException
from starlette.status import HTTP_403_FORBIDDEN
from app.core.config import db

guests_repo = GuestsRepository(db)
renters_repo = RentersRepository(db)
users_repo = UsersRepository(db)


async def authorize_guest(email):
    user = await users_repo.get_user_by_email(email=email)

    if not await authorize(user, "guest"):
        raise HTTPException(status_code=HTTP_403_FORBIDDEN)

    return user


async def authorize_renter(email):
    user = await users_repo.get_user_by_email(email=email)

    if not await authorize(user, "renter"):
        raise HTTPException(status_code=HTTP_403_FORBIDDEN)

    return user


async def authorize_guest_or_renter(email):
    user = await users_repo.get_user_by_email(email=email)

    if not await authorize(user, "guest", "renter"):
        raise HTTPException(status_code=HTTP_403_FORBIDDEN)

    return user


async def authorize(user, *roles) -> bool:
    return user.role in [role.lower() for role in roles]
