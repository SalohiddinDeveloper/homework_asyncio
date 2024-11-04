import asyncio

async def fetch_data(source_name, delay):
    await asyncio.sleep(delay)
    return f"Ma'lumot {source_name} dan"

async def main():
    task1 = asyncio.create_task(fetch_data("manba_1", 2))
    task2 = asyncio.create_task(fetch_data("manba_2", 3))
    task3 = asyncio.create_task(fetch_data("manba_3", 1))
    natijalar = await asyncio.gather(task1, task2, task3)
    print(natijalar)

asyncio.run(main())
