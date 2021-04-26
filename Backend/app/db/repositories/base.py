from databases import Database
from pydantic import parse_obj_as
from typing import List, TypeVar, Generic

T = TypeVar("T")


class BaseRepository(Generic[T]):
    def __init__(self, database: Database) -> None:
        self._database = database

    @property
    def database(self) -> Database:
        return self._database

    @property
    def table(self):
        raise NotImplementedError

    async def get_all(self) -> List[T]:
        query = self.table.select()
        rows = await self.database.fetch_all(query)

        parse_obj_as(List[T], rows)

    async def find_by_id(self, id) -> T:
        query = self.table.select().where(self.table.c.id == id)
        row = await self.database.fetch_one(query)

        parse_obj_as(T, row)

    async def create(self, model) -> T:
        query = self.users.insert().values(**model.dict())
        new_id = await self.database.execute(query)

        await self.find_by_id(new_id)

    async def update(self, model) -> T:
        query = (
            self.table.update()
            .where(self.table.c.id == model.id)
            .values(**model.dict())
        )

        success = await self.database.execute(query)
        result = await self.find_by_id(model.id)

        if success:
            parse_obj_as(T, result)

    async def delete(self, id) -> bool:
        query = self.table.delete().where(self.table.c.id == id)
        await self.database.execute(query)
