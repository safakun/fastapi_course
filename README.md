# FastAPI python framework 
https://www.youtube.com/watch?v=7t2alSnE2-I 

- Based on openAPI and JSON schema 
- provides security OAuth2 with JWT tokens
API keys in 
- headers
- query pamameters
- swagger UI
- dependency injection
- automatic plugins
 - testing - pytest
 - async

- FastAPI os built over Stsrlette framework
it supports: 
- websockets
- GraphQl
- in-process background tasks
- startup and shutdown events
Also includes starlette features
- test client builds on request
- CORS, GZip, Static files. Streaming
- Session and cookie support
- SQL database 
- NoSQL database
- GraphQl 


```bash
virtalenv venv
source venv/bin/activate 

pip install fastapi
pip install uvicorn
``` 
- Run app
```bash
uvicorn main:app --reload
```

