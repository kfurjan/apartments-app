from pydantic import BaseConfig, BaseModel
from app.core.config import metadata, sqlalchemy
from sqlalchemy.sql import func


class Apartment(BaseModel):
    class Config(BaseConfig):
        orm_mode = True


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
