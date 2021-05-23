from app.db.repositories.renters_and_guests_base import (
    RentersAndGuestsBaseRepository,
)
from app.db.repositories.base import BaseRepository
from app.models.domain.reservations import reservations
from app.models.domain.guests import guests


class ReservationsRepository(RentersAndGuestsBaseRepository):
    def table(self):
        return reservations

    async def guests_for_apartment(self, apartment_id: int):
        guests_ids = (
            self.table().where(apartment_id).select(self.table.c.guest_id).subquery()
        )
        query = guests.where(guests.c.id.in_(guests_ids))

        return await self.database.fetch_all(query)
