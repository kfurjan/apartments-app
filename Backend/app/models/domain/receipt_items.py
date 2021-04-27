from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from app.core.config import metadata, sqlalchemy
from sqlalchemy.sql import func


class ReceiptItemOut(BaseModel):
    id: int
    receipt_id: int
    service_id: int
    quantity: int
    created_at: datetime
    updated_at: datetime


class ReceiptItemInCreate(BaseModel):
    receipt_id: int
    service_id: int
    quantity: int


class ReceiptItemInUpdate(BaseModel):
    receipt_id: Optional[int]
    service_id: Optional[int]
    quantity: Optional[int]


receipt_items = sqlalchemy.Table(
    "receipt_items",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column(
        "receipt_id",
        sqlalchemy.Integer,
        sqlalchemy.ForeignKey("receipts.id"),
        nullable=False,
        index=True,
    ),
    sqlalchemy.Column(
        "service_id",
        sqlalchemy.Integer,
        sqlalchemy.ForeignKey("services.id"),
        nullable=False,
        index=True,
    ),
    sqlalchemy.Column("quantity", sqlalchemy.Integer),
    sqlalchemy.Column(
        "created_at", sqlalchemy.DateTime, nullable=False, server_default=func.now()
    ),
    sqlalchemy.Column(
        "updated_at",
        sqlalchemy.DateTime,
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    ),
)
