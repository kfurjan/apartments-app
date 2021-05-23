from app.db.repositories.base import BaseRepository
from app.models.domain.guests import guests


class GuestsRepository(BaseRepository):
    def table(self):
        return guests

    async def get_guest_for_user(self, user_id):
        query = self.table().select().where(self.table().c.user_id == user_id)
        model = await self.database.fetch_one(query)

        if model:
            return model
