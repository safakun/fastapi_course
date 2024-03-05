from typing import List
from fastapi import APIRouter 
from .. import schemas, models
from fastapi_sqlalchemy import DBSessionMiddleware, db 
from fastapi import FastAPI, status, Response, HTTPException

from ..repository import blog

router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
) 

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def destroy(id):
    blog = db.session.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'blog with id {id} not found')
    
    db.session.delete(blog)
    db.session.commit()
   
    return {f'Blog {id} was deleted'}
    
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
async def update(id, request: schemas.Blog):
    blog = db.session.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'blog with id {id} not found')
    else:
        db.session.query(models.Blog).filter(models.Blog.id == id).update(request.dict())
    
    db.session.commit()
    return 'updated'

@router.get('/', response_model=List[schemas.ShowBlog])
async def all_blogs():
    # return blog.get_all()
    blogs = db.session.query(models.Blog).all()
    return blogs 

@router.post('/', response_model=schemas.Blog, status_code=status.HTTP_201_CREATED)
async def blog(blog: schemas.Blog):
    # return blog.create()
    db_blog = models.Blog(title=blog.title, body=blog.body)
    db.session.add(db_blog)
    db.session.commit()
    return db_blog 

@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
async def show(id, response: Response):
    blog = db.session.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f'Blog with id {id} is not available')
        # response.status_code = status.HTTP_404_NOT_FOUND 
        # return {'detail': f'Blog with id {id} is not available'}
    return blog