import enum

from sqlalchemy import Column, Date, Enum, Integer, String

from database import Base


class Gender(str, enum.Enum):
    female = "female"
    male = "male"
    diverse = "diverse"


class Person(Base):
    __tablename__ = "person"

    id = Column(Integer, primary_key=True, index=True)
    name_first = Column(String(45))
    name_last = Column(String(45))
    gender = Column(Enum(Gender))
    date_of_birth = Column(Date)
    date_of_death = Column(Date)
    born_in = Column(String(45))
    memo = Column(String(64000))
