from typing import List
from fastapi import APIRouter 
from .. import schemas, models
from fastapi_sqlalchemy import DBSessionMiddleware, db 
from fastapi import FastAPI, status, Response, HTTPException 
from ..hashing import Hash

router = APIRouter(
    tags=['users']
) 


@router.post('/user', response_model=schemas.ShowUser)
async def create_user(request: schemas.User):
    
    new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.session.add(new_user)
    db.session.commit()
    db.session.refresh(new_user)
    return new_user


@router.get('/user/{id}', response_model=schemas.ShowUser)
async def get_user(id: int):
    user = db.session.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f'User with id {id} is not available')
    
    return user