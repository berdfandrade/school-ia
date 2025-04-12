from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from app.config.database import Base
import enum

class UserType(str, enum.Enum):
    student = "student"
    teacher = "teacher"
    admin = "admin"

class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    type = Column(Enum(UserType), nullable=False)
