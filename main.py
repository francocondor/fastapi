from fastapi import FastAPI, Path, Query
from fastapi.responses import HTMLResponse, JSONResponse, PlainTextResponse
from pydantic import BaseModel, Field
from typing import Optional, List
import datetime

app = FastAPI()

class Movie(BaseModel):
    id: int
    title: str
    overview: str
    year: int
    rating: float
    category: str

class MovieCreate(BaseModel):
    id: int
    title: str = Field(min_length=5, max_length=15)
    overview: str = Field(min_length=15, max_length=80)
    year: int = Field(le=datetime.datetime.now().year, ge=1900)
    rating: float = Field(ge=0, le=10)
    category: str = Field(min_length=5, max_length=20)

    model_config = {
        'json_schema_extra': {
            'example': {
                'id': 1,
                'title': 'Predestination',
                'overview': 'A temporal agent embarks on a final time-traveling assignment.',
                'year': 2014,
                'rating': 7.5,
                'category': 'Action'
            }
        }

    }

class MovieUpdate(BaseModel):
    title: Optional[str]
    overview: Optional[str]
    year: Optional[int]
    rating: Optional[float]
    category: Optional[str]

lista_movies: List[Movie] = []

@app.get("/html", tags=["HTML"])
def html():
    return HTMLResponse('<h1>Hello World</h1>')

@app.get("/", tags=["Home"])
def home():
    return PlainTextResponse(content='Home')

@app.get("/movies", tags=["Movies"])
def get_movies()-> List[Movie]:
    content = [item.model_dump() for item in lista_movies]
    return JSONResponse(content=content)

@app.get("/movies/{id}", tags=["Movies"])
def get_movie(id: int = Path(gt=0))-> Movie | dict:
    for movie in lista_movies:
        if movie.id == id:
            return JSONResponse(content=movie.model_dump())
    return JSONResponse(content={})

# http://localhost:5000/movies/?category=a
@app.get("/movies/", tags=["Movies"])
def get_movie_by_category(category: str = Query(min_length=5, max_length=20))-> Movie | dict:
    for movie in lista_movies:
        if movie.category == category :
            return JSONResponse(content=movie.model_dump())
    return JSONResponse(content={})

@app.post('/movies', tags=["Movies"])
def create_movie(movie: MovieCreate)-> List[Movie]:
    lista_movies.append(movie)
    content = [item.model_dump() for item in lista_movies]
    return JSONResponse(content=content)

@app.put('/movies/{id}', tags=["Movies"])
def update_movie(id: int, movie: MovieUpdate)-> List[Movie]:
    for item in lista_movies:
        if item.id == id:
            item.title    = movie.title
            item.overview = movie.overview
            item.year     = movie.year
            item.rating   = movie.rating
            item.category = movie.category
    content = [item.model_dump() for item in lista_movies]
    return JSONResponse(content=content)

@app.delete('/movies/{id}', tags=["Movies"])
def delete_movie(id: int)-> List[Movie]:
    for movie in lista_movies:
        if movie.id == id:
            lista_movies.remove(movie)
    content = [item.model_dump() for item in lista_movies]
    return JSONResponse(content=content)