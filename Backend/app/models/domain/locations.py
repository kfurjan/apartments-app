from datetime import datetime, time
from typing import Optional
from pydantic import BaseModel
from app.core.config import metadata, sqlalchemy
from sqlalchemy.sql import func


class LocationOut(BaseModel):
    id: int
    title: str
    description: str
    type_id: int
    working_hours_monday: time
    working_hours_tuesday: time
    working_hours_wednesday: time
    working_hours_thursday: time
    working_hours_friday: time
    working_hours_saturday: time
    working_hours_sunday: time
    additional_details: Optional[dict]
    city: str
    created_at: datetime
    updated_at: datetime


class LocationInCreate(BaseModel):
    title: str
    description: str
    type_id: int
    working_hours_monday: time
    working_hours_tuesday: time
    working_hours_wednesday: time
    working_hours_thursday: time
    working_hours_friday: time
    working_hours_saturday: time
    working_hours_sunday: time
    additional_details: Optional[dict]
    city: str


class LocationInUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    type_id: Optional[int]
    working_hours_monday: Optional[time]
    working_hours_tuesday: Optional[time]
    working_hours_wednesday: Optional[time]
    working_hours_thursday: Optional[time]
    working_hours_friday: Optional[time]
    working_hours_saturday: Optional[time]
    working_hours_sunday: Optional[time]
    additional_details: Optional[dict]
    city: Optional[str]


locations = sqlalchemy.Table(
    "locations",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("title", sqlalchemy.Text, nullable=False),
    sqlalchemy.Column("description", sqlalchemy.Text),
    sqlalchemy.Column(
        "type_id",
        sqlalchemy.Integer,
        sqlalchemy.ForeignKey("types.id"),
        nullable=False,
        index=True,
    ),
    sqlalchemy.Column("working_hours_monday", sqlalchemy.Text),
    sqlalchemy.Column("working_hours_tuesday", sqlalchemy.Text),
    sqlalchemy.Column("working_hours_wednesday", sqlalchemy.Text),
    sqlalchemy.Column("working_hours_thursday", sqlalchemy.Text),
    sqlalchemy.Column("working_hours_friday", sqlalchemy.Text),
    sqlalchemy.Column("working_hours_saturday", sqlalchemy.Text),
    sqlalchemy.Column("working_hours_sunday", sqlalchemy.Text),
    sqlalchemy.Column("additional_details", sqlalchemy.JSON),
    sqlalchemy.Column("city", sqlalchemy.Text, nullable=False),
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
