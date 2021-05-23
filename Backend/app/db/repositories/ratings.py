from app.db.repositories.base import BaseRepository
from app.models.domain.ratings import ratings


class RatingsRepository(BaseRepository):
    def table(self):
        return ratings

    async def get_all_for_apartment(self, apartment_id):
        query = self.table().select().where(self.table().c.apartment_id == apartment_id)
        return await self.database.fetch_all(query)
