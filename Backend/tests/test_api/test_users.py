import pytest
from starlette.status import HTTP_200_OK
from httpx import AsyncClient

EMAIL = "email"
ACCESS_TOKEN = "access_token"
USER_API_ENDPOINT = "/api/v1/user"
PASSWORD_DIGEST = "password_digest"
TEST_USER = {"email": "test@test.test", "password_digest": "test"}

jwt_token = ""
pytestmark = pytest.mark.asyncio


@pytest.mark.order(1)
async def test_create_user(async_client: AsyncClient):
    response = await async_client.post(url=USER_API_ENDPOINT, json=TEST_USER)
    json_response = response.json()

    assert response.status_code == HTTP_200_OK
    assert ACCESS_TOKEN in json_response

    global jwt_token
    jwt_token = json_response[ACCESS_TOKEN]


@pytest.mark.order(2)
async def test_get_user(async_client: AsyncClient):
    response = await async_client.get(
        url=USER_API_ENDPOINT, headers={"Authorization": f"Bearer {jwt_token}"}
    )
    json_response = response.json()

    assert response.status_code == HTTP_200_OK
    assert EMAIL in json_response
    assert PASSWORD_DIGEST in json_response
    assert json_response[EMAIL] == TEST_USER[EMAIL]
