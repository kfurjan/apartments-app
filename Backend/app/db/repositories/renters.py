from app.db.repositories.base import BaseRepository
from app.models.domain.renters import RenterOut, renters


class RentersRepository(BaseRepository):
    def table(self):
        return renters

    async def get_renter_for_user(self, user_id):
        query = self.table().select().where(self.table().c.user_id == user_id)
        model = await self.database.fetch_one(query)

        if model:
            return RenterOut(**model)
