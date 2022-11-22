import uvicorn
from fastapi import FastAPI
from magazine.Movie import Movie
from magazine.Link import Link
from magazine.Rating import Rating
from magazine.Tag import Tag

app = FastAPI()
movies_data = Movie.get_movies()
links_data = Link.get_links()
ratings_data = Rating.get_ratings()
tag_data = Tag.get_tags()


@app.get('/movies')
async def movies():
    return movies_data


@app.get('/links')
async def links():
    return links_data


@app.get('/ratings')
async def ratings():
    return ratings_data


@app.get('/tags')
async def tags():
    return tag_data


@app.get('/')
async def root():
    return {"message": "hello world"}

# links to working app: https://python-api-zaaw-programowanie.herokuapp.com/
# if __name__ == "__main__":
#     uvicorn.run(app, host="localhost", port=8000)
