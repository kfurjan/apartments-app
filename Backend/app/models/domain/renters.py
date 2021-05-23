from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from app.core.config import metadata, sqlalchemy
from sqlalchemy.sql import func


class RenterOut(BaseModel):
    id: int
    user_id: int
    address: str
    city: str
    first_name: str
    last_name: str
    oib: str
    date_of_birth: datetime
    created_at: datetime
    updated_at: datetime


class RenterInCreate(BaseModel):
    user_id: Optional[int]
    address: str
    city: str
    first_name: str
    last_name: str
    oib: str
    date_of_birth: datetime


class RenterInUpdate(BaseModel):
    user_id: Optional[int]
    address: Optional[str]
    city: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    oib: Optional[str]
    date_of_birth: Optional[datetime]


renters = sqlalchemy.Table(
    "renters",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
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
    sqlalchemy.Column("address", sqlalchemy.Text),
    sqlalchemy.Column("city", sqlalchemy.Text),
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
