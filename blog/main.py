from fastapi import FastAPI, status, Response, HTTPException
from . import schemas, models
from fastapi_sqlalchemy import DBSessionMiddleware, db

import os
from dotenv import load_dotenv

from typing import List
from .hashing import Hash

from .routers import blog


load_dotenv('.env')


app = FastAPI()

# to avoid csrftokenError
app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URL'])

# creating models
# models.Base.metadata.create_all(engine)
app.include_router(blog.router)



# @app.post('/blog', response_model=schemas.Blog, status_code=status.HTTP_201_CREATED, tags=['blogs'])
# async def blog(blog: schemas.Blog):
#     db_blog = models.Blog(title=blog.title, body=blog.body)
#     db.session.add(db_blog)
#     db.session.commit()
#     return db_blog

# @app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['blogs'])
# async def destroy(id):
#     blog = db.session.query(models.Blog).filter(models.Blog.id == id).first()
#     if not blog:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'blog with id {id} not found')
    
#     db.session.delete(blog)
#     db.session.commit()
   
#     return {f'Blog {id} was deleted'}
    
# @app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['blogs'])
# async def update(id, request: schemas.Blog):
#     blog = db.session.query(models.Blog).filter(models.Blog.id == id).first()
#     if not blog:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'blog with id {id} not found')
#     else:
#         db.session.query(models.Blog).filter(models.Blog.id == id).update(request.dict())
    
#     db.session.commit()
#     return 'updated'


# imcluding router 
# app.include_router(blog.router)
# @app.get('/blog', response_model=List[schemas.ShowBlog], tags=['blogs'])
# async def blog():
#     blogs = db.session.query(models.Blog).all()
#     return blogs



# @app.get('/blog/{id}', status_code=200, response_model=schemas.ShowBlog, tags=['blogs'])
# async def show(id, response: Response):
#     blog = db.session.query(models.Blog).filter(models.Blog.id == id).first()
#     if not blog:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f'Blog with id {id} is not available')
#         # response.status_code = status.HTTP_404_NOT_FOUND 
#         # return {'detail': f'Blog with id {id} is not available'}
#     return blog




@app.post('/user', response_model=schemas.ShowUser, tags=['users'])
async def create_user(request: schemas.User):
    
    new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.session.add(new_user)
    db.session.commit()
    db.session.refresh(new_user)
    return new_user


@app.get('/user/{id}', response_model=schemas.ShowUser, tags=['users'])
async def get_user(id: int):
    user = db.session.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f'User with id {id} is not available')
    
    return user
