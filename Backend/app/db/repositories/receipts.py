from app.db.repositories.base import BaseRepository
from app.models.domain.receipts import Receipt, receipts


class ReceiptsRepository(BaseRepository[Receipt]):
    def table(self):
        receipts
