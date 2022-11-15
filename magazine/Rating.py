import csv


class Rating:
    def __init__(self, user_id: int, movie_id: int, rating: float, timestamp: str):
        self.user = user_id
        self.movie_id = movie_id
        self.rating = rating
        self.timestamp = timestamp

    @classmethod
    def get_ratings(cls):
        ratings: list[Rating] = []

        with open('data/ratings.csv', 'r', newline='', encoding='UTF-8') as file:
            file.readline()  # skip first line
            reader = csv.reader(file, quotechar='|')
            for row in reader:
                user_id = int(row[0])
                movie_id = int(row[1])
                rating = float(row[2])
                timestamp = row[3]
                ratings.append(Rating(user_id, movie_id, rating, timestamp))
        return ratings
