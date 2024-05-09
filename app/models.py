from db import Base
from sqlalchemy import Column, Integer, Boolean, String


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=False)
    name = Column(String, nullable=False)
    biography = Column(String, nullable=True)
    is_admin = Column(Boolean, default=False)

