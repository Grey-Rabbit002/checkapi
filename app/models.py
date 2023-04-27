from .databases import Base
from sqlalchemy import Column,Integer,String,TIMESTAMP
class TeacherModel(Base) :
    __tablename__ = "teacher"
    id = Column(Integer,primary_key=True,nullable=False)
    dept_id = Column(Integer,nullable=False)
    teacher_name = Column(String,nullable=False)
    section = Column(String,nullable=False)
    title = Column(String,nullable=False)
    content = Column(String,nullable=False)
    created_at =  Column(TIMESTAMP(timezone=True),nullable=False,server_default=str('now()'))

class UserModel(Base) :
    __tablename__ = "user"
    id = Column(Integer,primary_key=True,nullable=False)
    email = Column(String,nullable=False,unique=True)
    password = Column(String,nullable=False)
    dept_id = Column(String,nullable=False)
    username = Column(String,nullable=False)