from app.db.repositories.base import BaseRepository
from app.models.domain.apartment_details import apartment_details


class ApartmentDetailsRepository(BaseRepository):
    def table(self):
        return apartment_details
