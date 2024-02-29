from fastapi import FastAPI 


app = FastAPI()

@app.get('/')
def index():
    return {'data': 'blog list'} 

@app.get('/blog/unpublished')
def unpublished():
    return {'data': {'all unpublished blogs'}}

@app.get('/blog/{id}')
# fetch blog with id = id
def about(id: int):
    return {'data': id}  



@app.get('/blog/{id}/comments')
# fetch comments for blog with id = id
def comments(id):
    return {'data': {'1', '2'}} 