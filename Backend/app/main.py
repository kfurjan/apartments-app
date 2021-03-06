from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from starlette.exceptions import HTTPException
from starlette.middleware.cors import CORSMiddleware

from app.api.errors.authjwt_exception_handler import authjwt_exception_handler
from app.api.errors.http_error import http_error_handler
from app.api.errors.validation_error import http422_error_handler
from app.api.routes.api import router as api_router
from app.core.config import (
    ALLOWED_HOSTS,
    API_PREFIX,
    APP_VERSION,
    DEBUG,
    PROJECT_NAME,
    db,
    jwt_token_denylist,
)
from app.models.common.jwt import Settings

app = FastAPI(title=PROJECT_NAME, debug=DEBUG, version=APP_VERSION)

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_HOSTS or ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@AuthJWT.load_config
def get_config():
    return Settings()


@AuthJWT.token_in_denylist_loader
def check_if_token_in_denylist(decrypted_token):
    return decrypted_token["jti"] in jwt_token_denylist


app.add_exception_handler(HTTPException, http_error_handler)
app.add_exception_handler(RequestValidationError, http422_error_handler)
app.add_exception_handler(AuthJWTException, authjwt_exception_handler)

app.include_router(api_router, prefix=API_PREFIX)


@app.on_event("startup")
async def startup():
    await db.connect()


@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()
