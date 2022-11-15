import csv


class Link:
    def __init__(self, link_id: int, imdb_id: int, tmdb_id: int):
        self.link_id = link_id
        self.imdb_id = imdb_id
        self.tmdb_id = tmdb_id

    @classmethod
    def get_links(cls):
        links: list[Link] = []

        with open('data/links.csv', 'r', newline='', encoding='UTF-8') as file:
            file.readline()  # skip first line
            reader = csv.reader(file, quotechar='|')
            for row in reader:
                link_id = int(row[0]) if row[0] != '' else None
                imdb_id = int(row[1]) if row[1] != '' else None
                tmdb_id = int(row[2]) if row[2] != '' else None
                links.append(Link(link_id, imdb_id, tmdb_id))
        return links
