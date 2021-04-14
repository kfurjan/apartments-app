from pydantic import BaseConfig, BaseModel
from app.core.config import metadata, sqlalchemy
from sqlalchemy.sql import func


class ApartmentDetail(BaseModel):
    class Config(BaseConfig):
        orm_mode = True


apartment_details = sqlalchemy.Table(
    "apartment_details",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("title", sqlalchemy.Text),
    sqlalchemy.Column("address", sqlalchemy.Text),
    sqlalchemy.Column("city", sqlalchemy.Text),
    sqlalchemy.Column("postal_code", sqlalchemy.Text),
    sqlalchemy.Column("latitude", sqlalchemy.Numeric),
    sqlalchemy.Column("longitude", sqlalchemy.Numeric),
    sqlalchemy.Column("description", sqlalchemy.Text),
    sqlalchemy.Column("price_per_night", sqlalchemy.Numeric),
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
