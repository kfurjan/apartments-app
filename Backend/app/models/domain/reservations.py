from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from app.core.config import metadata, sqlalchemy
from sqlalchemy.sql import func


class ReservationOut(BaseModel):
    id: int
    guest_id: int
    apartment_id: int
    number_of_guests: int
    starts_at: datetime
    ends_at: datetime
    additional_details: Optional[dict]
    created_at: datetime
    updated_at: datetime


class ReservationInCreate(BaseModel):
    guest_id: int
    apartment_id: int
    number_of_guests: int
    starts_at: datetime
    ends_at: datetime
    additional_details: Optional[dict]


class ReservationInUpdate(BaseModel):
    guest_id: Optional[int]
    apartment_id: Optional[int]
    number_of_guests: Optional[int]
    starts_at: Optional[datetime]
    ends_at: Optional[datetime]
    additional_details: Optional[dict]


reservations = sqlalchemy.Table(
    "reservations",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column(
        "guest_id",
        sqlalchemy.Integer,
        sqlalchemy.ForeignKey("guests.id"),
        nullable=False,
        index=True,
    ),
    sqlalchemy.Column(
        "apartment_id",
        sqlalchemy.Integer,
        sqlalchemy.ForeignKey("apartments.id"),
        nullable=False,
        index=True,
    ),
    sqlalchemy.Column("number_of_guests", sqlalchemy.Integer, nullable=False),
    sqlalchemy.Column("starts_at", sqlalchemy.DateTime),
    sqlalchemy.Column("ends_at", sqlalchemy.DateTime),
    sqlalchemy.Column("additional_details", sqlalchemy.Text),
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
