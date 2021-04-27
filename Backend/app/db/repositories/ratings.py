from app.db.repositories.base import BaseRepository
from app.models.domain.ratings import ratings


class RatingsRepository(BaseRepository):
    def table(self):
        return ratings
