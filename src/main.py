from fastapi import FastAPI, Depends, Query
from fastapi.requests import Request
from fastapi.responses import HTMLResponse, PlainTextResponse, FileResponse, Response, JSONResponse
from src.routers.movie_router import movie_router
from src.utils.http_error_handle import HTTPErrorHandler
from typing import Annotated

from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

def dependency1():
    print('Global dependency 1')

def dependency2():
    print('Global dependency 2')

app = FastAPI(dependencies=[Depends(dependency1), Depends(dependency2)]) # Global dependencies

app.add_middleware(HTTPErrorHandler)
# @app.middleware('http')
# async def http_error_handler(request: Request, call_next)-> Response | JSONResponse:
#     print('Middleware is running!')
#     return await call_next(request)

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

# def common_params(start_date: str, end_date: str):
#     return {"start_date": start_date, "end_date": end_date}
# CommonDep = Annotated[dict, Depends(common_params)]

class CommonDep:
    def __init__(self, start_date: str, end_date: str):
        self.start_date = start_date
        self.end_date = end_date

@app.get('/users', tags=["Users"])
def get_users(commons: CommonDep = Depends()):
    return f"Users created between {commons.start_date} and {commons.end_date}"

@app.get('/customers', tags=["Customers"])
def get_customers(commons: CommonDep = Depends()):
    return f"Customers created between {commons.start_date} and {commons.end_date}"

@app.get('/get_file', tags=["Files"])
def get_file():
    return FileResponse('README.md')

app.include_router(prefix='/movies', router=movie_router)