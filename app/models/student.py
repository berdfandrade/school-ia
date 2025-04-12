from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, String, Enum
from app.models.user import User


class Student(User):

    __tablename__ = "students"

    id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    public_id = Column(Integer)
    school_id = Column(String)

    __mapper__args__ = {
        "polymorphic_identity": "student",
        "polymorphic_on": User.type
    }




