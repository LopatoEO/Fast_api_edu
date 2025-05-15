#На вход подается словарь user_data. Напишите модель Pydantic для этого словаря,
# сериализуйте словарь в JSON и десериализуйте JSON обратно в экземпляр модели.

from pydantic import BaseModel, EmailStr

user_data = {"id": 1, "name": "Иван", "email": "ivan@example.com"}

class UserData(BaseModel):
    id : int
    name : str
    email : EmailStr


UserD = UserData(**user_data)
print(UserD)
print(UserD.model_dump_json())