from app.db.repositories.base import BaseRepository
from app.models.domain.apartment_details import apartment_details


class ApartmentDetailsRepository(BaseRepository):
    def table(self):
        return apartment_details

    async def get_for_apartment(self, apartment_id):
        query = self.table().select().where(self.table().c.apartment_id == apartment_id)
        return await self.database.fetch_one(query)
