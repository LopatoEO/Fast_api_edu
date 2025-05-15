#На вход подается словарь order_data.
# Напишите модели Pydantic для этого словаря, учитывая список элементов.
# Сериализуйте и десериализуйте словарь.

from pydantic import BaseModel

order_data = {"items": [{"name": "Яблоко", "price": 1.5}, {"name": "Банан", "price": 2.0}]}

class Item(BaseModel):
    name : str
    price : float

class Order(BaseModel):
    items: list[Item]

order = Order(**order_data)
print(order)
print(order.model_dump_json())