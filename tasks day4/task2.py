#На вход подается словарь user_data и словарь user_data2.
# Напишите модель Pydantic для этих словарей, учитывая,
# что поле age необязательное. Сериализуйте оба словаря

from pydantic import BaseModel
from typing import Optional

user_data = {"id": 1, "name": "Иван", "email": "ivan@example.com", "age": 30}
user_data2 = {"id": 2, "name": "Петр", "email": "petr@example.com"}

class UserData(BaseModel):
    id : int
    name : str
    email : str
    age: Optional[int] = None


Users = [UserData(**user_data), UserData(**user_data2)]
print(Users)
print([item.model_dump_json() for item in Users])