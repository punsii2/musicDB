from sqlalchemy import Column, Integer, String

from database import Base


class Role(Base):
    __tablename__ = "role"

    id = Column(Integer, primary_key=True, index=True)
    role = Column(String(255))
    type = Column(String(8))
