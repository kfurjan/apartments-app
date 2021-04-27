from app.db.repositories.base import BaseRepository
from app.models.domain.locations import locations


class LocationsRepository(BaseRepository):
    def table(self):
        return locations
