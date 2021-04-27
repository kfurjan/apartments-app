from app.db.repositories.base import BaseRepository
from app.models.domain.reservations import reservations


class ReservationsRepository(BaseRepository):
    def table(self):
        return reservations
