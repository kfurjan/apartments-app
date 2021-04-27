from app.db.repositories.base import BaseRepository
from app.models.domain.apartments import apartments


class ApartmentsRepository(BaseRepository):
    def table(self):
        return apartments
