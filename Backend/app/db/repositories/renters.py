from app.db.repositories.base import BaseRepository
from app.models.domain.renters import renters


class RentersRepository(BaseRepository):
    def table(self):
        return renters
