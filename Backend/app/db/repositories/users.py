from app.db.errors import EntityDoesNotExist
from app.db.repositories.base import BaseRepository
from app.models.domain.users import User, users


class UsersRepository(BaseRepository):
    def table(self):
        return users

    async def get_user_by_email(self, *, email: str) -> User:
        query = users.select().where(users.c.email == email)
        user_row = await self.database.fetch_one(query)

        if user_row:
            return User(**user_row)

        raise EntityDoesNotExist(f"User with email {email} does not exist")

    async def get_user(self, *, user: User) -> User:
        query = users.select().where(
            users.c.email == user.email
            and users.c.password_digest == user.password_digest
        )
        user_row = await self.database.fetch_one(query)

        if user_row:
            return User(**user_row)

        raise EntityDoesNotExist("User does not exist")

    async def create_user(self, *, user: User) -> User:
        query = users.insert().values(**user.dict())
        user_id = await self.database.execute(query)

        query = users.select().where(users.c.id == user_id)
        user_row = await self.database.fetch_one(query)

        if user_row:
            return User(**user_row)
