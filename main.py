from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

lista_movies = [
    {
        "id": 1,
        "title": "Avatar",
        "director": "James Cameron",
        "overview": "A paraplegic marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.",
        "year": 2009,
        "rating": 7.8,
        "category": "Action"
    },
    {
        "id": 2,
        "title": "The Shawshank Redemption",
        "director": "Frank Darabont",
        "overview": "Two imprisoned",
        "year": 1994,
        "rating": 9.3,
        "category": "Drama"
    }
]

@app.get("/html", tags=["Home"])
def html():
    return HTMLResponse('<h1>Hello World</h1>')

@app.get("/", tags=["Home"])
def home():
    return "Hello World"

@app.get("/movies", tags=["Home"])
def get_movies():
    return lista_movies

@app.get("/movies/{id}", tags=["Home"])
def get_movie(id: int):
    for movie in lista_movies:
        if movie['id'] == id:
            return movie
    return []
