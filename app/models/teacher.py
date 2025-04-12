from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, String, Enum
from app.models.user import User


class Teacher(User):

    __tablename__ = "teachers"

    id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    public_id = Column(Integer)
    subject = Column(String)

    __mapper__args__ = {
        "polymorphic_identity": "teacher",
        "polymorphic_on": User.type
    }




