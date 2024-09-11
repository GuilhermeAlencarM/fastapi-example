from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Enum
from sqlalchemy.orm import deferred
from config.database import Base
import bcrypt


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True, nullable=False)
    password = deferred(Column(String, nullable=False))
    is_admin = Column(Boolean, nullable=False)

