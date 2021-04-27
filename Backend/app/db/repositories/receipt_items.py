from app.db.repositories.base import BaseRepository
from app.models.domain.receipt_items import receipt_items


class ReceiptItemsRepository(BaseRepository):
    def table(self):
        return receipt_items
