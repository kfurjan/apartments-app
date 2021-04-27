from app.db.repositories.base import BaseRepository
from app.models.domain.apartments import Apartment, apartments


class ApartmentsRepository(BaseRepository[Apartment]):
    def table(self):
        return apartments
