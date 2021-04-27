from app.db.repositories.base import BaseRepository
from app.models.domain.renters import Renter, renters


class RentersRepository(BaseRepository[Renter]):
    def table(self):
        return renters
