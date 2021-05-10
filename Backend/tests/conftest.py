from typing import Iterator

import pytest
from app.main import app
from asgi_lifespan import LifespanManager
from httpx import AsyncClient


@pytest.fixture()
async def async_client() -> Iterator[AsyncClient]:
    async with LifespanManager(app):
        async with AsyncClient(app=app, base_url="http://test") as async_client:
            yield async_client
