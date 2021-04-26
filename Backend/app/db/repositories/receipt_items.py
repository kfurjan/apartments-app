from app.db.repositories.base import BaseRepository
from app.models.domain.receipt_items import ReceiptItem, receipt_items


class ReceiptItemsRepository(BaseRepository[ReceiptItem]):
    def table(self):
        receipt_items
