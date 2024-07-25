from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import HTMLResponse, PlainTextResponse, FileResponse, Response, JSONResponse
from src.routers.movie_router import movie_router
from src.utils.http_error_handle import HTTPErrorHandler

app = FastAPI()

# app.add_middleware(HTTPErrorHandler)
@app.middleware('http')
async def http_error_handler(request: Request, call_next)-> Response | JSONResponse:
    print('Middleware is running!')
    return await call_next(request)

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