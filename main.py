from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", tags=["Home"])
def home():
    return "Hello World"

@app.get("/movies", tags=["Home"])
def movies():
    return {"Hello": "World"}

@app.get("/html", tags=["Home"])
def html():
    return HTMLResponse('<h1>Hello World</h1>')