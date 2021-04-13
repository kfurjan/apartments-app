from pydantic import BaseConfig, BaseModel
from app.core.config import metadata, sqlalchemy
from sqlalchemy.sql import func


class Locations(BaseModel):
    class Config(BaseConfig):
        orm_mode = True


locations = sqlalchemy.Table(
    "locations",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("title", sqlalchemy.Text, nullable=False),
    sqlalchemy.Column("description", sqlalchemy.Text),
    sqlalchemy.Column(
        "type_id",
        sqlalchemy.Integer,
        sqlalchemy.ForeignKey("types.id"),
        nullable=False,
        index=True,
    ),
    sqlalchemy.Column("working_hours_monday", sqlalchemy.Text),
    sqlalchemy.Column("working_hours_tuesday", sqlalchemy.Text),
    sqlalchemy.Column("working_hours_wednesday", sqlalchemy.Text),
    sqlalchemy.Column("working_hours_thursday", sqlalchemy.Text),
    sqlalchemy.Column("working_hours_friday", sqlalchemy.Text),
    sqlalchemy.Column("working_hours_saturday", sqlalchemy.Text),
    sqlalchemy.Column("working_hours_sunday", sqlalchemy.Text),
    sqlalchemy.Column("additional_details", sqlalchemy.JSON),
    sqlalchemy.Column("city", sqlalchemy.Text, nullable=False),
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
