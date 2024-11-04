
import asyncio

async def tez_task():
    await asyncio.sleep(1)
    return "Tez tugadi"

async def sekin_task():
    await asyncio.sleep(5)
    return "Sekin tugadi"

async def main():
    fast = asyncio.create_task(tez_task())
    slow = asyncio.create_task(sekin_task())
    natijalar = await asyncio.gather(fast, slow)
    print(natijalar)

asyncio.run(main())
