from app.db.repositories.reservations import reservations
from typing import List

from app.db.repositories.base import BaseRepository
from app.models.domain.apartments import ApartmentOut, ApartmentsQueryParams, apartments
from sqlalchemy.sql.expression import and_, column, select


class ApartmentsRepository(BaseRepository):
    def table(self):
        return apartments

    async def get_all_filtered(
        self, params: ApartmentsQueryParams
    ) -> List[ApartmentOut]:
        filters = [
            column(key) == value
            for key, value in params.dict(exclude_unset=True, exclude_none=True).items()
        ]

        return await self.database.fetch_all(
            self.table().select().where(and_(*filters))
        )

    async def get_unavailable_dates(self, id):
        query = select([reservations.c.starts_at, reservations.c.ends_at]).where(
            reservations.c.apartment_id == id
        )
        return await self.database.fetch_all(query)
