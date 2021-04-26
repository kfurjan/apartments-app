from app.db.repositories.base import BaseRepository
from app.models.domain.apartment_details import ApartmentDetail, apartment_details


class ApartmentDetailsRepository(BaseRepository[ApartmentDetail]):
    def table(self):
        apartment_details
