from sqlalchemy import Column, Integer, String
from database import Base 

class Marks(Base):
    __tablename__ = "student"

    student_id = Column(Integer, primary_key=True)
    name = Column(String)
    marks = Column(Integer)


class Coaches(Base):
    __tablename__ = "coaches"

    coach_id = Column(Integer, primary_key=True)
    name = Column(String)
    section = Column(String)
    subject = Column(String)
