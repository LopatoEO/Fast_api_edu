# TODO: Создайте 4 корутины, каждая из которых возвращает строку.
#  Запустите их параллельно и соберите результаты в список.


import asyncio
import random


async def string_returner(str: str):
    delay = random.randint(1, 2)
    await asyncio.sleep(delay)
    return str


stringdist = ['один', 'два', 'три', 'четыре']


async def main(strings: list):
    result = []
    tasks = [string_returner(item) for item in strings]
    for task in asyncio.as_completed(tasks):
        result.append(await task)
    return result

if __name__ == '__main__':
    print(asyncio.run(main(stringdist)))
