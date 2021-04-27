from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from app.core.config import metadata, sqlalchemy
from sqlalchemy.sql import func


class ServiceOut(BaseModel):
    id: int
    name: str
    description: str
    price: float
    created_at: datetime
    updated_at: datetime


class ServiceInCreate(BaseModel):
    name: str
    description: str
    price: float


class ServiceInUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]
    price: Optional[float]


services = sqlalchemy.Table(
    "services",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.Text),
    sqlalchemy.Column("description", sqlalchemy.Text),
    sqlalchemy.Column("price", sqlalchemy.Numeric),
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
