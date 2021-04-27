from app.db.repositories.base import BaseRepository
from app.models.domain.locations import Location, locations


class LocationsRepository(BaseRepository[Location]):
    def table(self):
        return locations
