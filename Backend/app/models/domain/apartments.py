from datetime import datetime, date
from typing import Optional
from pydantic import BaseModel
from app.core.config import metadata, sqlalchemy
from sqlalchemy.sql import func


class ApartmentOut(BaseModel):
    id: int
    title: Optional[str]
    address: Optional[str]
    city: Optional[str]
    postal_code: Optional[str]
    latitude: Optional[float]
    longitude: Optional[float]
    description: Optional[str]
    price_per_night: Optional[int]
    available: Optional[bool]
    availability_start_date: Optional[date]
    availability_end_date: Optional[date]
    renter_id: Optional[int]
    images: Optional[dict]
    created_at: datetime
    updated_at: datetime


class ApartmentInCreate(BaseModel):
    title: str
    address: str
    city: str
    postal_code: str
    latitude: float
    longitude: float
    description: str
    price_per_night: int
    available: bool
    availability_start_date: date
    availability_end_date: date
    renter_id: int
    images: Optional[dict]


class ApartmentInUpdate(BaseModel):
    title: Optional[str]
    address: Optional[str]
    city: Optional[str]
    postal_code: Optional[str]
    latitude: Optional[float]
    longitude: Optional[float]
    description: Optional[str]
    price_per_night: Optional[int]
    available: Optional[bool]
    availability_start_date: Optional[date]
    availability_end_date: Optional[date]
    renter_id: Optional[int]
    images: Optional[dict]


apartments = sqlalchemy.Table(
    "apartments",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("title", sqlalchemy.Text, nullable=False),
    sqlalchemy.Column("address", sqlalchemy.Text, nullable=False),
    sqlalchemy.Column("city", sqlalchemy.Text, nullable=False),
    sqlalchemy.Column("postal_code", sqlalchemy.Text, nullable=False),
    sqlalchemy.Column("latitude", sqlalchemy.Numeric, nullable=False),
    sqlalchemy.Column("longitude", sqlalchemy.Numeric, nullable=False),
    sqlalchemy.Column("description", sqlalchemy.Text),
    sqlalchemy.Column("price_per_night", sqlalchemy.Numeric, nullable=False),
    sqlalchemy.Column("available", sqlalchemy.Boolean),
    sqlalchemy.Column("availability_start_date", sqlalchemy.Date),
    sqlalchemy.Column("availability_end_date", sqlalchemy.Date),
    sqlalchemy.Column(
        "renter_id",
        sqlalchemy.Integer,
        sqlalchemy.ForeignKey("renters.id"),
        nullable=False,
        index=True,
    ),
    sqlalchemy.Column("images", sqlalchemy.JSON),
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
