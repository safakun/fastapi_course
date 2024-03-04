from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db
import os
from dotenv import load_dotenv
from .routers import blog, user

load_dotenv('.env')

app = FastAPI()

# to avoid csrftokenError
app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URL'])

app.include_router(blog.router)
app.include_router(user.router)

