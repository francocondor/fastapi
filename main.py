from fastapi import FastAPI

app = FastAPI()

@app.get("/", tags=["Home"])
def home():
    return "Hello World"

@app.get("/movies", tags=["Home"])
def home():
    return {"Hello": "World"}