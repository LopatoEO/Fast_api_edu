import asyncio
import random

async def wait_random():
    delay = random.randint(1, 5)
    await asyncio.sleep(delay)
    print(f"Задача завершилась через {delay} секунд")


# TODO: дана асинхронная функция которая ждет случайное количество секунд (от 1 до 5)
#  Создайте 3 корутины, и запустите их асинхронно с помощью asyncio.gather().

async def main():
    for i in range(3):
        await asyncio.create_task(wait_random())


if __name__ == '__main__':
    asyncio.run(main())
