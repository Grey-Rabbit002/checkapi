from sqlalchemy.orm import Session
from  app.databases import get_db
from fastapi import HTTPException,status,Depends,APIRouter
from .. import models
route = APIRouter()

@route.get("/posts/show")
async def posts(db:Session = Depends(get_db)):
    results = db.query(models.TeacherModel).all()
    if not results :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No Post Found")
    
    return results