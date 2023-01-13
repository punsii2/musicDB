from typing import Optional
from pydantic import BaseModel
from datetime import date
from models.person import Gender


class BasePerson(BaseModel):
    name_first: str
    name_last: str
    gender: Gender
    date_of_birth: date
    date_of_death: date
    born_in: str
    memo: str


class CreatePerson(BasePerson):
    pass


class Person(BasePerson):
    id: int

    class Config:
        orm_mode = True
        use_enum_values = True
