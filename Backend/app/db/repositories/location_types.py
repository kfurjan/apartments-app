from app.db.repositories.base import BaseRepository
from app.models.domain.location_types import location_types


class LocationTypesRepository(BaseRepository):
    def table(self):
        return location_types
