from pydantic import BaseConfig, BaseModel
from app.core.config import metadata, sqlalchemy
from sqlalchemy.sql import func


class Receipt(BaseModel):
    class Config(BaseConfig):
        orm_mode = True


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
