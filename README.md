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

uvicorn blog.main:app --reload
``` 

```bash
pip install -r requirements.txt
virtualenv blog-env 

```

- **See a Swagger and redoc documentation**
[FastAPI swagger UI](http://localhost:8000/docs).
[FastAPI REDOC documentaion](http://localhost:8000/redoc).

- it changes dynamically  

- [Installe TablePlus on Ubuntu](https://tableplus.com/blog/2019/10/tableplus-linux-installation.html)


```bash
# Add TablePlus gpg key
wget -qO - https://deb.tableplus.com/apt.tableplus.com.gpg.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/tableplus-archive.gpg > /dev/null

# Add TablePlus repo
sudo add-apt-repository "deb [arch=amd64] https://deb.tableplus.com/debian/22 tableplus main"

# Install
sudo apt update
sudo apt install tableplus

```

TODO 

- need to add POSTGRESQL to fastAPi via docker compose 

