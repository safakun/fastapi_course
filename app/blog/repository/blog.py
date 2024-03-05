from .. import schemas, models
from fastapi_sqlalchemy import DBSessionMiddleware, db 

async def get_all():
    blogs = db.session.query(models.Blog).all()
    return blogs 

async def create(request: schemas.Blog):
    db_blog = models.Blog(blog.dict())
    db.session.add(db_blog)
    db.session.commit()
    return db_blog 
