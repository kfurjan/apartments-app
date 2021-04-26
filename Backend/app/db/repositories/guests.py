from app.db.repositories.base import BaseRepository
from app.models.domain.guests import Guest, guests


class GuestsRepository(BaseRepository[Guest]):
    def table(self):
        guests
