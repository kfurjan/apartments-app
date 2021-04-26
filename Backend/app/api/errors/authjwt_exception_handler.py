from fastapi import Request
from fastapi_jwt_auth.exceptions import AuthJWTException
from starlette.responses import JSONResponse


def authjwt_exception_handler(_: Request, exc: AuthJWTException) -> JSONResponse:
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.message})
