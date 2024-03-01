from fastapi import FastAPI 
from . import schemas, models
from .database import engine


app = FastAPI()

# creating models
models.Base.metadata.create_all(engine)



@app.post('/blog') 
def create(request: schemas.Blog):
    return {'title': request.title, 'body': request.body}