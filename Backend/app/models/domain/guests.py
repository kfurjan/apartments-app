from pydantic import BaseConfig, BaseModel
from app.core.config import metadata, sqlalchemy
from sqlalchemy.sql import func


class Guest(BaseModel):
    class Config(BaseConfig):
        orm_mode = True


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
