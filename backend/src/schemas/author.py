from typing import Optional
from pydantic import BaseModel


class BaseAuthor(BaseModel):
    work_id: int
    person_id: int
    role_id: int


class CreateAuthor(BaseAuthor):
    pass


class Author(BaseAuthor):
    id: int

    class Config:
        orm_mode = True
