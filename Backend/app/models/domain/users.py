from pydantic import BaseConfig, BaseModel
from pydantic.networks import EmailStr
from app.core.config import metadata, sqlalchemy
from sqlalchemy.sql import func


class User(BaseModel):
    email: EmailStr
    password_digest: str

    class Config(BaseConfig):
        orm_mode = True


users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column(
        "email", sqlalchemy.Text, unique=True, nullable=False, index=True
    ),
    sqlalchemy.Column("password_digest", sqlalchemy.Text, nullable=False),
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
