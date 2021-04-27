from app.db.repositories.base import BaseRepository
from app.models.domain.receipts import receipts


class ReceiptsRepository(BaseRepository):
    def table(self):
        return receipts
