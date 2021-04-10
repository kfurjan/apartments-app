from asyncpg import Connection, Record


class UsersQueries:
    async def get_user_by_email(self, conn: Connection, *, email: str) -> Record: ...
    async def create_new_user(
        self, conn: Connection, *, email: str, password: str
    ) -> Record: ...


class Queries(
    UsersQueries,
): ...


queries: Queries
