#На вход подается словарь user_data.
# Напишите модели Pydantic для этого словаря,
# учитывая вложенный адрес. Сериализуйте и десериализуйте словарь.

from pydantic import BaseModel

user_data = {
    "id": 1,
    "name": "Иван",
    "email": "ivan@example.com",
    "address": {"street": "Тверская", "city": "Москва", "zip_code": "123456"}
}

class Address(BaseModel):
    street: str
    city : str
    zip_code: str

class UserData(BaseModel):
    id : int
    name : str
    email : str
    address : Address


UserD = UserData(**user_data)
print(UserD)
print(UserD.model_dump_json())