from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel
from app.core.config import metadata, sqlalchemy
from sqlalchemy.sql import func


class GuestOut(BaseModel):
    id: int
    documents: Optional[dict]
    user_id: Optional[int]
    first_name: str
    last_name: str
    oib: str
    date_of_birth: date
    created_at: datetime
    updated_at: datetime


class GuestInCreate(BaseModel):
    documents: Optional[dict]
    user_id: Optional[int]
    first_name: str
    last_name: str
    oib: str
    date_of_birth: str


class GuestInUpdate(BaseModel):
    documents: Optional[dict]
    user_id: Optional[int]
    first_name: Optional[str]
    last_name: Optional[str]
    oib: Optional[str]
    date_of_birth: Optional[str]


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
    sqlalchemy.Column("first_name", sqlalchemy.Text),
    sqlalchemy.Column("last_name", sqlalchemy.Text),
    sqlalchemy.Column("oib", sqlalchemy.Text),
    sqlalchemy.Column("date_of_birth", sqlalchemy.Text),
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
