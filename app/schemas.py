from pydantic import BaseModel

class Post(BaseModel) :
    dept_id : int
    teacher_name : str
    section : str
    title = str
    content = str