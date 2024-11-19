from fetch_data import fetch_data
import pytest
import asyncio  # noqa: F401


@pytest.mark.asyncio
async def test_fetch_data():
    result = await fetch_data()
    assert result == {"data": "some data"}
