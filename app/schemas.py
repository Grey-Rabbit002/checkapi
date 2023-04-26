from pydantic import BaseModel

class Post(BaseModel) :
    dept_id : int
    teacher_name : str
    section : str
    title : str
    content : str

class CreatePost(Post) :
    pass

class ResponsePost(Post) :
    class Config :
        orm_mode = True

class UpdatePost(Post) :
    pass
