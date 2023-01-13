from sqlalchemy import Column, ForeignKey, Integer

from database import Base


class Author(Base):
    __tablename__ = "author"

    id = Column(Integer, primary_key=True, index=True)
    work_id = Column(
        Integer,
        # ForeignKey("work.id"), # XXX Table does not exist yet!
    )
    person_id = Column(Integer, ForeignKey("person.id"))
    role_id = Column(Integer, ForeignKey("role.id"))
