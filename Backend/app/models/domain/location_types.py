from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from app.core.config import metadata, sqlalchemy
from sqlalchemy.sql import func


class LocationTypeOut(BaseModel):
    id: int
    type: str
    created_at: datetime
    updated_at: datetime


class LocationTypeInCreate(BaseModel):
    type: str


class LocationTypeInUpdate(BaseModel):
    type: Optional[str]


location_types = sqlalchemy.Table(
    "location_types",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("type", sqlalchemy.Text, nullable=False),
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
