from fastapi import FastAPI, status, Response 
from . import schemas, models
from fastapi_sqlalchemy import DBSessionMiddleware, db

import os
from dotenv import load_dotenv

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

@app.get('/blog')
async def blog():
    blogs = db.session.query(models.Blog).all()
    return blogs

@app.get('/blog/{id}', status_code=200)
async def show(id, response: Response):
    blog = db.session.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        response.status_code = status.HTTP_404_NOT_FOUND 
        return {'detail': f'Blog with id {id} is not available'}
    return blog

# @app.post('/blog') 
# def create(request: schemas.Blog):
#     return {'title': request.title, 'body': request.body}