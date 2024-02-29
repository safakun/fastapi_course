from fastapi import FastAPI 
from pydantic import BaseModel


app = FastAPI()

class Blog(BaseModel):
    title: str
    body: str

@app.post('/blog') 
def create(request: Blog):
    return {'title': request.title, 'body': request.body}