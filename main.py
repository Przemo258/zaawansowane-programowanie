import uvicorn
from fastapi import FastAPI
from magazine.Movie import Movie
from magazine.Link import Link
from magazine.Rating import Rating
from magazine.Tag import Tag

app = FastAPI()


@app.get('/movies')
async def movies():
    return Movie.get_movies()


@app.get('/links')
async def links():
    return Link.get_links()


@app.get('/ratings')
async def ratings():
    return Rating.get_ratings()


@app.get('/tags')
async def tags():
    return Tag.get_tags()


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
