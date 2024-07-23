from fastapi import FastAPI

app = FastAPI()

@app.get("/", tags=["Home"])
def home():
    return "Hello World"