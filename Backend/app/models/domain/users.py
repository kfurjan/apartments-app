from pydantic import BaseConfig, BaseModel
from app.core.config import metadata, sqlalchemy


class User(BaseModel):
    email: str
    password: str

    class Config(BaseConfig):
        orm_mode = True


users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column(
        "email", sqlalchemy.Text, unique=True, nullable=False, index=True
    ),
    sqlalchemy.Column("password", sqlalchemy.Text),
)
