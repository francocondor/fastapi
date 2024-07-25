from fastapi import FastAPI
from fastapi.responses import HTMLResponse, PlainTextResponse, FileResponse
from src.routers.movie_router import movie_router

app = FastAPI()

@app.get("/html", tags=["HTML"])
def html():
    return HTMLResponse('<h1>Hello World</h1>')

@app.get("/", tags=["Home"])
def home():
    return PlainTextResponse(content='Home', status_code=200)

@app.get('/get_file', tags=["Files"])
def get_file():
    return FileResponse('README.md')

app.include_router(prefix='/movies', router=movie_router)