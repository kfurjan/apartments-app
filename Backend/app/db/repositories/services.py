from app.db.repositories.base import BaseRepository
from app.models.domain.services import services


class ServicesRepository(BaseRepository):
    def table(self):
        return services
