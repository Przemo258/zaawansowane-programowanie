import csv


class Movie:
    def __init__(self, movie_id: int, title: str, genres: list[str]):
        self.movie_id = movie_id
        self.title = title
        self.genres = genres

    @classmethod
    def get_movies(cls):
        movies: list[Movie] = []

        with open('data/movies.csv', 'r', newline='', encoding='UTF-8') as file:
            file.readline()  # skip first line
            reader = csv.reader(file, quotechar='|')
            for row in reader:
                movie_id = int(row[0])
                title = row[1]
                genres = row[2].split('|')
                movies.append(Movie(movie_id, title, genres))
        return movies
