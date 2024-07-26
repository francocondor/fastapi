from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import HTMLResponse, PlainTextResponse, FileResponse, Response, JSONResponse
from src.routers.movie_router import movie_router
from src.utils.http_error_handle import HTTPErrorHandler

from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()

# app.add_middleware(HTTPErrorHandler)
@app.middleware('http')
async def http_error_handler(request: Request, call_next)-> Response | JSONResponse:
    print('Middleware is running!')
    return await call_next(request)

static_path = os.path.join(os.path.dirname(__file__), 'static')
templates_path = os.path.join(os.path.dirname(__file__), 'templates')

app.mount('/static', StaticFiles(directory=static_path), name='static')
templates = Jinja2Templates(directory=templates_path)

@app.get("/html", tags=["HTML"])
def html():
    return HTMLResponse('<h1>Hello World</h1>')

@app.get("/", tags=["Home"])
def home(request: Request):
    return templates.TemplateResponse('index.html', {'message': 'Welcome', 'request': request})

@app.get('/get_file', tags=["Files"])
def get_file():
    return FileResponse('README.md')

app.include_router(prefix='/movies', router=movie_router)