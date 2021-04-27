from app.db.repositories.base import BaseRepository
from app.models.domain.reservations import Reservation, reservations


class ReservationsRepository(BaseRepository[Reservation]):
    def table(self):
        return reservations
