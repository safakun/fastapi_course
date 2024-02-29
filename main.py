from fastapi import FastAPI 
from typing import Optional 
from pydantic import BaseModel
import uvicorn


app = FastAPI()

@app.get('/blog')
def index(limit=10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {'data': f'{limit} published blogs from db'} 
    else:
        return {'data': f'{limit} published blogs from db'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data': {'all unpublished blogs'}}

@app.get('/blog/{id}')
# fetch blog with id = id
def about(id: int):
    return {'data': id}  



@app.get('/blog/{id}/comments')
# fetch comments for blog with id = id
def comments(id, limit=10):
    return limit 


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post('/blog')
def create_blog(blog: Blog):
    return {'data': f'Blog is created with a title as {blog.title}'} 


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=9000)