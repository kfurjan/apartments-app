from pydantic import BaseConfig, BaseModel


class User(BaseModel):
    email: str
    username: str

    class Config(BaseConfig):
        orm_mode = True
