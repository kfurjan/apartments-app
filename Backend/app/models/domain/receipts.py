from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from app.core.config import metadata, sqlalchemy
from sqlalchemy.sql import func


class ReceiptOut(BaseModel):
    id: int
    receipt_number: str
    total: float
    guest_id: int
    renter_id: int
    created_at: datetime
    updated_at: datetime


class ReceiptInCreate(BaseModel):
    receipt_number: str
    total: float
    guest_id: int


class ReceiptInUpdate(BaseModel):
    receipt_number: Optional[str]
    total: Optional[float]
    guest_id: Optional[int]
    renter_id: Optional[int]


receipts = sqlalchemy.Table(
    "receipts",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("receipt_number", sqlalchemy.Text),
    sqlalchemy.Column("total", sqlalchemy.Numeric),
    sqlalchemy.Column(
        "guest_id",
        sqlalchemy.Integer,
        sqlalchemy.ForeignKey("guests.id"),
        nullable=False,
        index=True,
    ),
    sqlalchemy.Column(
        "renter_id",
        sqlalchemy.Integer,
        sqlalchemy.ForeignKey("renters.id"),
        nullable=False,
        index=True,
    ),
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
