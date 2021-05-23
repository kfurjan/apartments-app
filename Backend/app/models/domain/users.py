from typing import Optional
from pydantic import BaseModel
from pydantic.networks import EmailStr
from app.core.config import metadata, sqlalchemy
from sqlalchemy.sql import func


class UserInLogin(BaseModel):
    email: str
    password_digest: str


class UserOut(BaseModel):
    id: int
    email: str
    password_digest: str
    role: str


class UserInCreate(BaseModel):
    email: EmailStr
    password_digest: str
    role: str


class UserInUpdate(BaseModel):
    email: Optional[str]
    password_digest: Optional[str]
    role: Optional[str]


users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column(
        "email", sqlalchemy.Text, unique=True, nullable=False, index=True
    ),
    sqlalchemy.Column("password_digest", sqlalchemy.Text, nullable=False),
    sqlalchemy.Column("role", sqlalchemy.Text, nullable=False),
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
