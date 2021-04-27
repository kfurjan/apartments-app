from app.db.repositories.base import BaseRepository
from app.models.domain.services import Service, services


class ServicesRepository(BaseRepository[Service]):
    def table(self):
        return services
