from app.db.repositories.base import BaseRepository


class RentersAndGuestsBaseRepository(BaseRepository):
    async def get_all_for_renter(self, renter_id):
        query = self.table().select().where(self.table().c.renter_id == renter_id)
        return await self.database.fetch_all(query)

    async def get_all_for_guest(self, guest_id):
        query = self.table().select().where(self.table().c.guest_id == guest_id)
        return await self.database.fetch_all(query)
