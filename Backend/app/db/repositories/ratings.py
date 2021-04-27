from app.db.repositories.base import BaseRepository
from app.models.domain.ratings import Rating, ratings


class RatingsRepository(BaseRepository[Rating]):
    def table(self):
        return ratings
