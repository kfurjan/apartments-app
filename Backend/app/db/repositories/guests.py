from app.db.repositories.base import BaseRepository
from app.models.domain.guests import guests


class GuestsRepository(BaseRepository):
    def table(self):
        return guests
