from app.db.repositories.renters_and_guests_base import RentersAndGuestsBaseRepository
from app.db.repositories.base import BaseRepository
from app.models.domain.receipts import receipts


class ReceiptsRepository(RentersAndGuestsBaseRepository):
    def table(self):
        return receipts
