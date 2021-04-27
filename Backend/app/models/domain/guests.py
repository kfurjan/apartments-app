from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from app.core.config import metadata, sqlalchemy
from sqlalchemy.sql import func


class GuestOut(BaseModel):
    id: int
    documents: Optional[dict]
    user_id: Optional[int]
    created_at: datetime
    updated_at: datetime


class GuestInCreate(BaseModel):
    documents: Optional[dict]
    user_id: int


class GuestInUpdate(BaseModel):
    documents: Optional[dict]
    user_id: Optional[int]


guests = sqlalchemy.Table(
    "guests",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("documents", sqlalchemy.JSON),
    sqlalchemy.Column(
        "user_id",
        sqlalchemy.Integer,
        sqlalchemy.ForeignKey("users.id"),
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
