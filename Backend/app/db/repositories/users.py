from app.db.errors import EntityDoesNotExist
from app.db.queries.queries import queries
from app.db.repositories.base import BaseRepository
from app.models.domain.users import User


class UsersRepository(BaseRepository):
    async def get_user_by_email(self, *, email: str) -> User:
        user_row = await queries.get_user_by_email(self.connection, email=email)
        if user_row:
            return User(**user_row)

        raise EntityDoesNotExist(f"user with email {email} does not exist")

    async def create_user(
        self,
        *,
        email: str,
        password: str,
    ) -> User:
        user = User(email=email, password=password)

        async with self.connection.transaction():
            user_row = await queries.create_new_user(
                self.connection, email=user.email, password=password
            )

        return user.copy(update=dict(user_row))
