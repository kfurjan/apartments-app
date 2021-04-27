from databases import Database
from app.db.errors import EntityDoesNotExist


class BaseRepository:
    def __init__(self, database: Database) -> None:
        self._database = database

    @property
    def database(self) -> Database:
        return self._database

    def table(self):
        raise NotImplementedError

    async def get_all(self):
        query = self.table().select()
        return await self.database.fetch_all(query)

    async def find_by_id(self, id):
        query = self.table().select().where(self.table().c.id == id)
        model = await self.database.fetch_one(query)

        if model:
            return model

        raise EntityDoesNotExist(f"entity with id: {id} does not exist")

    async def create(self, model):
        query = self.table().insert().values(**model.dict())
        new_id = await self.database.execute(query)

        return await self.find_by_id(new_id)

    async def update(self, id, model):
        query = (
            self.table()
            .update()
            .where(self.table().c.id == id)
            .values(**model.dict(exclude_unset=True))
        )

        await self.database.execute(query)
        return await self.find_by_id(model.id)

    async def delete(self, id):
        query = self.table().delete().where(self.table().c.id == id)
        return await self.database.execute(query)
