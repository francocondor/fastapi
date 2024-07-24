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
    }
]

@app.get("/", tags=["Home"])
def home():
    return "Hello World"

@app.get("/movies", tags=["Home"])
def movies():
    return lista_movies

@app.get("/html", tags=["Home"])
def html():
    return HTMLResponse('<h1>Hello World</h1>')