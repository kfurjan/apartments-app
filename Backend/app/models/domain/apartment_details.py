from datetime import datetime, time
from typing import Optional
from pydantic import BaseModel
from app.core.config import metadata, sqlalchemy
from sqlalchemy.sql import func


class ApartmentDetailOut(BaseModel):
    id: int
    apartment_id: Optional[int]
    checkout_time: Optional[time]
    on_land: Optional[bool]
    square_meters: Optional[float]
    number_of_rooms: Optional[int]
    wifi_present: Optional[bool]
    tv_present: Optional[bool]
    parking_included: Optional[bool]
    rating: Optional[float]
    additional_details: Optional[dict]
    created_at: datetime
    updated_at: datetime


class ApartmentDetailInCreate(BaseModel):
    apartment_id: Optional[int]
    checkout_time: Optional[time]
    on_land: Optional[bool]
    square_meters: Optional[float]
    number_of_rooms: Optional[int]
    wifi_present: Optional[bool]
    tv_present: Optional[bool]
    parking_included: Optional[bool]
    rating: Optional[float]
    additional_details: Optional[dict]


class ApartmentDetailInUpdate(BaseModel):
    apartment_id: Optional[int]
    checkout_time: Optional[time]
    on_land: Optional[bool]
    square_meters: Optional[float]
    number_of_rooms: Optional[int]
    wifi_present: Optional[bool]
    tv_present: Optional[bool]
    parking_included: Optional[bool]
    rating: Optional[float]
    additional_details: Optional[dict]


apartment_details = sqlalchemy.Table(
    "apartment_details",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column(
        "apartment_id",
        sqlalchemy.Integer,
        sqlalchemy.ForeignKey("apartments.id"),
        nullable=False,
        index=True,
    ),
    sqlalchemy.Column("checkout_time", sqlalchemy.Time),
    sqlalchemy.Column("on_land", sqlalchemy.Boolean),
    sqlalchemy.Column("square_meters", sqlalchemy.Numeric),
    sqlalchemy.Column("number_of_rooms", sqlalchemy.Integer),
    sqlalchemy.Column("wifi_present", sqlalchemy.Boolean),
    sqlalchemy.Column("tv_present", sqlalchemy.Boolean),
    sqlalchemy.Column("parking_included", sqlalchemy.Boolean),
    sqlalchemy.Column("rating", sqlalchemy.Numeric),
    sqlalchemy.Column("additional_details", sqlalchemy.JSON),
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
