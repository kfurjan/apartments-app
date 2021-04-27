from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from app.core.config import metadata, sqlalchemy
from sqlalchemy.sql import func


class RatingOut(BaseModel):
    id: int
    rated_by_user_id: int
    rating: float
    comment: int
    subject_id: int
    subject_type: str
    created_at: datetime
    updated_at: datetime


class RatingInCreate(BaseModel):
    rated_by_user_id: int
    rating: float
    comment: int
    subject_id: int
    subject_type: str


class RatingInUpdate(BaseModel):
    rated_by_user_id: Optional[int]
    rating: Optional[float]
    comment: Optional[int]
    subject_id: Optional[int]
    subject_type: Optional[str]


ratings = sqlalchemy.Table(
    "ratings",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column(
        "rated_by_user_id",
        sqlalchemy.Integer,
        sqlalchemy.ForeignKey("users.id"),
        nullable=False,
        index=True,
    ),
    sqlalchemy.Column("rating", sqlalchemy.Numeric, nullable=False),
    sqlalchemy.Column("comment", sqlalchemy.Text),
    sqlalchemy.Column("subject_id", sqlalchemy.Integer, nullable=False),
    sqlalchemy.Column("subject_type", sqlalchemy.Text, nullable=False),
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
