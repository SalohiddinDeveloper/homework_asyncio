import asyncio

async def send_message(user_name, message, delay):
    await asyncio.sleep(delay)
    print(f"{user_name} yubordi: {message}")

async def main():
    msg1 = asyncio.create_task(send_message("foydalanuvchi_1", "salom", 1))
    msg2 = asyncio.create_task(send_message("foydalanuvchi_2", "qalay", 2))
    msg3 = asyncio.create_task(send_message("foydalanuvchi_3", "xayr", 3))
    await asyncio.gather(msg1, msg2, msg3)

asyncio.run(main())
