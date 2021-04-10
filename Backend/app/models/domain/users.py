from pydantic import BaseConfig, BaseModel


class User(BaseModel):
    email: str
    password: str

    class Config(BaseConfig):
        orm_mode = True
