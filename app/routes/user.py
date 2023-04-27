from fastapi import HTTPException,status,Depends,APIRouter
from sqlalchemy.orm import Session
from .. import schemas,databases,models,utils



route = APIRouter()

@route.post("/users/create",status_code=status.HTTP_201_CREATED,response_model=schemas.responseUser)
def createUser(new_user : schemas.createUser,db:Session = Depends(databases.get_db)) :
    user = models.UserModel(**new_user.dict())
    hashed_password = utils.hash(new_user.password)
    user.password = hashed_password
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@route.get("/users/getSpecific/{id}",response_model = schemas.responseUser)
def get_user(id:int,db : Session = Depends(databases.get_db)) :
    user = db.query(models.UserModel).filter(models.UserModel.id == id).first()
    if not user :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found")
    return user

