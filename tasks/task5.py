# TODO: Создайте корутину, которая ждет 5 секунд.
#  Запустите ее как задачу и отмените ее через 2 секунды.

import asyncio


async def my_coroutine():
    await asyncio.sleep(5)


async def main():
    task = asyncio.create_task(my_coroutine())
    await asyncio.sleep(2)
    task.cancel()
    print(f"Задача отменена: {task.cancelled()}")


if __name__ == '__main__':
    asyncio.run(main())