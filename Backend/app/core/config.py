from typing import List

import sqlalchemy
from app.resources.strings import (
    ALLOWED_HOSTS_ENV,
    DB_CONNECTION,
    DEBUG_ENV,
    ENVIRONMENT_FILE,
    MAX_CONNECTIONS_COUNT_ENV,
    MIN_CONNECTIONS_COUNT_ENV,
    PROJECT_NAME_DESC,
    PROJECT_NAME_ENV,
    SECRET_KEY_ENV,
)
from databases import Database, DatabaseURL
from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings, Secret

API_VERSION = "/v1"
API_PREFIX = f"/api{API_VERSION}"
APP_VERSION = "0.1.0"

JWT_TOKEN_PREFIX = "Token"

config = Config(ENVIRONMENT_FILE)

DEBUG: bool = config(DEBUG_ENV, cast=bool, default=False)
SECRET_KEY: Secret = config(SECRET_KEY_ENV, cast=Secret)

DATABASE_URL: DatabaseURL = config(DB_CONNECTION, cast=DatabaseURL)
MIN_CONNECTIONS_COUNT: int = config(MIN_CONNECTIONS_COUNT_ENV, cast=int, default=10)
MAX_CONNECTIONS_COUNT: int = config(MAX_CONNECTIONS_COUNT_ENV, cast=int, default=10)

db = Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

PROJECT_NAME: str = config(PROJECT_NAME_ENV, default=PROJECT_NAME_DESC)
ALLOWED_HOSTS: List[str] = config(
    ALLOWED_HOSTS_ENV,
    cast=CommaSeparatedStrings,
    default="",
)
