from sqlalchemy import Column, ForeignKey, Integer, String

from database import Base


class PersonPerson(Base):
    __tablename__ = "person_person"

    id = Column(Integer, primary_key=True, index=True)
    pid_1 = Column(Integer, ForeignKey("person.id", ondelete="CASCADE"))
    pid_2 = Column(Integer, ForeignKey("person.id", ondelete="CASCADE"))
    type = Column(String(45))
