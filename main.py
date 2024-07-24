from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Movie(BaseModel):
    id: Optional[int] = None
    title: str
    overview: str
    year: int
    rating: float
    category: str

lista_movies = [
    {
        "id": 1,
        "title": "Avatar",
        "overview": "A paraplegic marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.",
        "year": 2009,
        "rating": 7.8,
        "category": "Action"
    },
    {
        "id": 2,
        "title": "The Shawshank Redemption",
        "overview": "Two imprisoned",
        "year": 1994,
        "rating": 9.3,
        "category": "Drama"
    }
]

@app.get("/html", tags=["HTML"])
def html():
    return HTMLResponse('<h1>Hello World</h1>')

@app.get("/", tags=["Home"])
def home():
    return "Hello World"

@app.get("/movies", tags=["Movies"])
def get_movies():
    return lista_movies

@app.get("/movies/{id}", tags=["Movies"])
def get_movie(id: int):
    for movie in lista_movies:
        if movie['id'] == id:
            return movie
    return []

# http://localhost:5000/movies/?category=a&year=1
@app.get("/movies/", tags=["Movies"])
def get_movie_by_category(category: str, year: int):
    for movie in lista_movies:
        if movie['category'] == category and movie['year'] == year:
            return movie
    return []

@app.post('/movies', tags=["Movies"])
def create_movie(movie: Movie):
    lista_movies.append(movie.model_dump())
    return lista_movies

@app.put('/movies/{id}', tags=["Movies"])
def update_movie(id: int, movie: Movie):
    for item in lista_movies:
        if item['id'] == id:
            item['title'] = movie.title
            item['overview'] = movie.overview
            item['year'] = movie.year
            item['rating'] = movie.rating
            item['category'] = movie.category
    return lista_movies

@app.delete('/movies/{id}', tags=["Movies"])
def delete_movie(id: int):
    for movie in lista_movies:
        if movie['id'] == id:
            lista_movies.remove(movie)
    return lista_movies