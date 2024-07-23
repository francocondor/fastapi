from fastapi import FastAPI

app = FastAPI()

app.title = "My First FastAPI App"
app.version = "2.0.0"

@app.get("/")
def home():
    return "Hello World"