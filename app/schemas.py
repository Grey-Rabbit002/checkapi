from pydantic import BaseModel,EmailStr

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


class createUser(BaseModel) :
    dept_id : str
    username : str
    email : EmailStr
    password : str

class responseUser(BaseModel) :
    dept_id : str
    username : str
    email : EmailStr
    class Config :
        orm_mode = True

