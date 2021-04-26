from app.db.repositories.base import BaseRepository
from app.models.domain.location_types import LocationType, location_types


class LocationTypesRepository(BaseRepository[LocationType]):
    def table(self):
        location_types
