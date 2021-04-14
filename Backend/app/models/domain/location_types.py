from pydantic import BaseConfig, BaseModel
from app.core.config import metadata, sqlalchemy
from sqlalchemy.sql import func


class LocationType(BaseModel):
    class Config(BaseConfig):
        orm_mode = True


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
