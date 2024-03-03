from fastapi import FastAPI, status, Response, HTTPException
from . import schemas, models
from fastapi_sqlalchemy import DBSessionMiddleware, db

import os
from dotenv import load_dotenv

from typing import List

from passlib.context import CryptContext

load_dotenv('.env')


app = FastAPI()

# to avoid csrftokenError
app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URL'])

# creating models
# models.Base.metadata.create_all(engine)


@app.post('/blog', response_model=schemas.Blog, status_code=status.HTTP_201_CREATED)
async def blog(blog: schemas.Blog):
    db_blog = models.Blog(title=blog.title, body=blog.body)
    db.session.add(db_blog)
    db.session.commit()
    return db_blog

@app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def destroy(id):
    blog = db.session.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'blog with id {id} not found')
    
    db.session.delete(blog)
    db.session.commit()
   
    return {f'Blog {id} was deleted'}
    
@app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED)
async def update(id, request: schemas.Blog):
    blog = db.session.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'blog with id {id} not found')
    else:
        db.session.query(models.Blog).filter(models.Blog.id == id).update(request.dict())
    
    db.session.commit()
    return 'updated'



@app.get('/blog', response_model=List[schemas.ShowBlog])
async def blog():
    blogs = db.session.query(models.Blog).all()
    return blogs

@app.get('/blog/{id}', status_code=200, response_model=schemas.ShowBlog)
async def show(id, response: Response):
    blog = db.session.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f'Blog with id {id} is not available')
        # response.status_code = status.HTTP_404_NOT_FOUND 
        # return {'detail': f'Blog with id {id} is not available'}
    return blog


pwd_txt = CryptContext(schemes=['bcrypt'], deprecated='auto')

@app.post('/user')
async def create_user(request: schemas.User):
    hashedPassword = pwd_txt.hash(request.password)
    new_user = models.User(name=request.name, email=request.email, password=hashedPassword)
    db.session.add(new_user)
    db.session.commit()
    db.session.refresh(new_user)
    return new_user
