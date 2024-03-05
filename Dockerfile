FROM python:3.9

WORKDIR /app
COPY . .
# COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
# RUN cd app
RUN alembic init alembic
RUN alembic revision --autogenerate -m "New Migration"
RUN alembic upgrade head
RUN uvicorn blog.main:app --host 0.0.0.0 --port 80


# 
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
# CMD ["alembic", "init", "alembic"]
# CMD ["alembic", "revision", "--autogenerate", "-m", "\"New Migration\""]
# CMD {"alembic", "upgrade", "head"}
# CMD ["uvicorn", "blog.main:app", "--reload"]
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]