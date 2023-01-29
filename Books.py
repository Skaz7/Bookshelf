from datetime import datetime


class Book:
    """Main Book class, other classes will inherit from this class"""

    def __init__(self, title, author, genre, year):
        self.title = title
        self.author = author
        self.genre = genre
        self.year = year
        self.entry_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id


class PrintedBook(Book):
    """Classic printed book class"""

    def __init__(self, title, author, genre, year, pages):
        super().__init__(title, author, genre, year)
        self.pages = pages


class EBook(Book):
    """Ebook class, with few additional parameters related to ebooks."""

    def __init__(
        self,
        title,
        author,
        genre,
        year,
        reading_status,
        eformat,
        device,
    ):
        super().__init__(title, author, genre, year, reading_status)
        self.format = eformat
        self.device = device


class Audiobook(Book):
    """Audiobook class, with few additional parameters related to audiobooks."""

    def __init__(self, title, author, genre, year, subscribed):
        super().__init__(title, author, genre, year)
        self.subscribed = subscribed
