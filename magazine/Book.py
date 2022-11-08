from magazine.Library import Library


class Book:
    def __init__(self, library: Library, publication_date: str,
                 author_name: str, author_surname: str,
                 number_of_pages: int):
        self.number_of_pages = number_of_pages
        self.author_surname = author_surname
        self.author_name = author_name
        self.publication_date = publication_date
        self.library = library

    def __str__(self):
        return f'This is a book by {self.author_name} {self.author_surname}' \
               ' published {self.publication_date} from {self.library} '
