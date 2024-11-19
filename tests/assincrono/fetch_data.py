import asyncio


async def fetch_data() -> dict:
    await asyncio.sleep(1)
    return {"data": "some data"}
