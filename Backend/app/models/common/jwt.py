from datetime import timedelta
from app.core.config import SECRET_KEY
from pydantic import BaseModel


class Settings(BaseModel):
    authjwt_secret_key: str = str(SECRET_KEY)
    authjwt_denylist_enabled: bool = True
    authjwt_denylist_token_checks: set = {"access"}
    access_expires: int = timedelta(minutes=120)
