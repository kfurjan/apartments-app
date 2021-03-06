import pytest
from httpx import AsyncClient
from starlette.status import (
    HTTP_401_UNAUTHORIZED,
    HTTP_404_NOT_FOUND,
    HTTP_422_UNPROCESSABLE_ENTITY,
)

pytestmark = pytest.mark.asyncio


async def test_404_error_handler(async_client: AsyncClient):
    response = await async_client.get("/wrong_path")

    assert response.status_code == HTTP_404_NOT_FOUND
    assert response.json() == {"errors": ["Not Found"]}


async def test_401_jwt_authorization_error_handler(async_client: AsyncClient):
    response = await async_client.get("/api/v1/user")

    assert response.status_code == HTTP_401_UNAUTHORIZED
    assert response.json() == {"detail": "Missing Authorization Header"}


async def test_422_jwt_authorization_error_handler(async_client: AsyncClient):
    response = await async_client.get(
        "/api/v1/user", headers={"Authorization": "Bearer wrong_token"}
    )
    assert response.status_code == HTTP_422_UNPROCESSABLE_ENTITY
    assert response.json() == {"detail": "Not enough segments"}

    response = await async_client.get(
        "/api/v1/user", headers={"Authorization": "token wrong_token"}
    )
    assert response.status_code == HTTP_422_UNPROCESSABLE_ENTITY
    assert response.json() == {
        "detail": "Bad Authorization header. Expected value 'Bearer <JWT>'"
    }
