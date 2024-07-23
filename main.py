from fastapi import FastAPI

app = FastAPI()

app.title = "My First FastAPI App"

@app.get("/")
def home():
    return "Hello World"