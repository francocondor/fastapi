from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse

app = FastAPI()

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
def create_movie(
    id: int = Body(),
    title: str = Body(),
    overview: str = Body(),
    year: int = Body(),
    rating: float = Body(),
    category: str = Body()
):
    lista_movies.append({
        "id": id,
        "title": title,
        "overview": overview,
        "year": year,
        "rating": rating,
        "category": category
    })
    return lista_movies

@app.put('/movies/{id}', tags=["Movies"])
def update_movie(
    id: int,
    title: str = Body(),
    overview: str = Body(),
    year: int = Body(),
    rating: float = Body(),
    category: str = Body()
):
    for movie in lista_movies:
        if movie['id'] == id:
            movie['title'] = title
            movie['overview'] = overview
            movie['year'] = year
            movie['rating'] = rating
            movie['category'] = category
    return lista_movies

@app.delete('/movies/{id}', tags=["Movies"])
def delete_movie(id: int):
    for movie in lista_movies:
        if movie['id'] == id:
            lista_movies.remove(movie)
    return lista_movies