from app.db.repositories.base import BaseRepository
from app.models.domain.receipt_items import receipt_items


class ReceiptItemsRepository(BaseRepository):
    def table(self):
        return receipt_items

    async def get_all_for_receipt(self, receipt_id):
        query = self.table().select().where(self.table().c.receipt_id == receipt_id)
        return await self.database.fetch_all(query)
