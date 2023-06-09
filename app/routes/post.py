from sqlalchemy.orm import Session
from  app.databases import get_db
from fastapi import HTTPException,status,Depends,APIRouter,Response
from .. import models,schemas
from typing import Optional
import datetime
route = APIRouter()

@route.get("/posts/show")
async def posts(db:Session = Depends(get_db),search_dept_id : Optional[str]= -1,search_section:Optional[str]= ""):
    results = db.query(models.TeacherModel).filter(models.TeacherModel.dept_id == search_dept_id,models.TeacherModel.section == search_section).limit(limit=5).all()
    if not results :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No Post Found")
    res = []
    curr_dateTime = datetime.datetime.now()
    for i in results :
        dt_object = datetime.datetime.fromisoformat(str(i.created_at).split('+')[0])
        print(dt_object)
        time_diff = curr_dateTime - dt_object
        minutes_diff = time_diff.total_seconds() // 60
        if minutes_diff <= 30 :
            res.append(i)

    return res

@route.post("/posts/create",status_code=status.HTTP_201_CREATED,response_model=schemas.ResponsePost)
async def createpost(new_post :schemas.CreatePost,db: Session = Depends(get_db)) :
    new_post = models.TeacherModel(dept_id = new_post.dept_id,teacher_name = new_post.teacher_name,section = new_post.section,title = new_post.title,content = new_post.content)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@ route.delete ("/posts/delete/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id:str,db:Session = Depends(get_db)):
    deleted_post = db.query(models.TeacherModel).filter(models.TeacherModel.id == id)
    if deleted_post.first() is None :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Post Not Found")
    deleted_post.delete(synchronize_session=  False)
    db.commit()
    return {Response(status_code=status.HTTP_204_NO_CONTENT)}

@route.put ("/posts/update/{id}",response_model=schemas.ResponsePost)
async def update_post(id :str, updated_post : schemas.UpdatePost,db:Session = Depends(get_db)) :
    post = db.query(models.TeacherModel).filter(models.TeacherModel.id == id)
    if  post.first() is None :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Post not found")
    # new_post_content = models.TeacherModel(dept_id = updated_post.dept_id,teacher_name = updated_post.teacher_name,section = updated_post.section,title = updated_post.title,content = updated_post.content)
    post.update(updated_post.dict(),synchronize_session=False)
    db.commit()
    return post.first()

@route.get("/posts/getSpecific/{id}",response_model=schemas.ResponsePost)
async def getSpecific(id:str,db:Session =Depends(get_db)) :
    post = db.query(models.TeacherModel).filter(models.TeacherModel.id == id).first()
    if not post :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No Such Activity Found")
    return post
