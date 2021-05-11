from datetime import date, datetime
from typing import Optional

from app.core.config import metadata, sqlalchemy
from fastapi.params import Query
from pydantic import BaseModel
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
    price_per_night: Optional[float]
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
    price_per_night: float
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
    price_per_night: Optional[float]
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


class ApartmentsQueryParams(BaseModel):
    address: Optional[str] = Query(None, title="Apartment's address")
    city: Optional[str] = Query(None, title="Apartment's city")
    postal_code: Optional[str] = Query(None, title="Apartment's postal code")
    latitude: Optional[float] = Query(None, title="Apartment's latitude")
    longitude: Optional[float] = Query(None, title="Apartment's longitude")
    price_per_night: Optional[float] = Query(None, title="Apartment's price")
    available: Optional[bool] = Query(None, title="Is apartment available")
    availability_start_date: Optional[date] = Query(None)
    availability_end_date: Optional[date] = Query(None)
