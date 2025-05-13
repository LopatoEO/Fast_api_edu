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
    tasks = [string_returner(item) for item in strings]
    results = await asyncio.gather(*tasks)
    return results

if __name__ == '__main__':
    asyncio.run(main(stringdist))
