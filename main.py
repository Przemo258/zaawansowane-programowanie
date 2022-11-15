import csv
from fastapi import FastAPI
import uvicorn
from magazine.Movie import Movie, get_movies

app = FastAPI()

movies: list[Movie] = get_movies()


@app.get('/movies')
async def root():
    return movies


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
