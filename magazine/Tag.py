import csv


class Tag:
    def __init__(self, user_id: int, movie_id: int, tag: str, timestamp: str):
        self.user = user_id
        self.movie_id = movie_id
        self.tag = tag
        self.timestamp = timestamp

    @classmethod
    def get_tags(cls):
        tags: list[Tag] = []

        with open('data/ratings.csv', 'r', newline='', encoding='UTF-8') as file:
            file.readline()  # skip first line
            reader = csv.reader(file, quotechar='|')
            for row in reader:
                user_id = int(row[0])
                movie_id = int(row[1])
                rating = row[2]
                timestamp = row[3]
                tags.append(Tag(user_id, movie_id, rating, timestamp))
        return tags
