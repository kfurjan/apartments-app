from datetime import datetime
from typing import Optional
from pydantic import BaseConfig, BaseModel
from pydantic.networks import EmailStr
from app.core.config import metadata, sqlalchemy
from sqlalchemy.sql import func


class User(BaseModel):
    email: EmailStr
    password_digest: str


class UserOut(BaseModel):
    id: int
    email: str
    password_digest: str
    first_name: str
    last_name: str
    oib: str
    date_of_birth: datetime
    created_at: datetime
    updated_at: datetime


class UserInCreate(BaseModel):
    email: str
    password_digest: str
    first_name: str
    last_name: str
    oib: str
    date_of_birth: datetime


class UserInUpdate(BaseModel):
    email: Optional[str]
    password_digest: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    oib: Optional[str]
    date_of_birth: Optional[datetime]


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
