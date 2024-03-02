from fastapi import FastAPI 
from . import schemas, models
# from .database import engine
from fastapi_sqlalchemy import DBSessionMiddleware, db

import os
from dotenv import load_dotenv

load_dotenv('.env')


app = FastAPI()

# to avoid csrftokenError
app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URL'])

# creating models
# models.Base.metadata.create_all(engine)


@app.post('/blog', response_model=schemas.Blog)
async def blog(blog: schemas.Blog):
    db_book = models.Blog(title=blog.title, body=blog.body)
    db.session.add(db_book)
    db.session.commit()
    return db_book

# @app.get('/book/')
# async def book():
#     book = db.session.query(ModelBook).all()
#     return book


# @app.post('/blog') 
# def create(request: schemas.Blog):
#     return {'title': request.title, 'body': request.body}