from pydantic import BaseConfig, BaseModel
from app.core.config import metadata, sqlalchemy
from sqlalchemy.sql import func


class Reservation(BaseModel):
    class Config(BaseConfig):
        orm_mode = True


reservations = sqlalchemy.Table(
    "reservations",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column(
        "guest_id",
        sqlalchemy.Integer,
        sqlalchemy.ForeignKey("guests.id"),
        nullable=False,
        index=True,
    ),
    sqlalchemy.Column(
        "apartment_id",
        sqlalchemy.Integer,
        sqlalchemy.ForeignKey("apartments.id"),
        nullable=False,
        index=True,
    ),
    sqlalchemy.Column("number_of_guests", sqlalchemy.Integer, nullable=False),
    sqlalchemy.Column("starts_at", sqlalchemy.DateTime),
    sqlalchemy.Column("ends_at", sqlalchemy.DateTime),
    sqlalchemy.Column("additional_details", sqlalchemy.Text),
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
