from app.resources.strings import (
    DB_CONNECTION,
    DEBUG_ENV,
    ENVIRONMENT_FILE,
    MAX_CONNECTIONS_COUNT_ENV,
    MIN_CONNECTIONS_COUNT_ENV,
    SECRET_KEY_ENV,
)
from databases import DatabaseURL
from starlette.config import Config
from starlette.datastructures import Secret

API_VERSION = "v1"
API_PREFIX = "/api"

JWT_TOKEN_PREFIX = "Token"

config = Config(ENVIRONMENT_FILE)

DEBUG: bool = config(DEBUG_ENV, cast=bool, default=False)
SECRET_KEY: Secret = config(SECRET_KEY_ENV, cast=Secret)

DATABASE_URL: DatabaseURL = config(DB_CONNECTION, cast=DatabaseURL)
MIN_CONNECTIONS_COUNT: int = config(MIN_CONNECTIONS_COUNT_ENV, cast=int, default=10)
MAX_CONNECTIONS_COUNT: int = config(MAX_CONNECTIONS_COUNT_ENV, cast=int, default=10)
