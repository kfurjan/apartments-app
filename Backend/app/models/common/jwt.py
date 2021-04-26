from app.core.config import SECRET_KEY
from pydantic import BaseModel


class Settings(BaseModel):
    authjwt_secret_key: str = SECRET_KEY
