# tests/test_main.py
import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_read_books():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/books")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
