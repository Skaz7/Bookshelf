class Book:
    """Main Book class, other classes will inherit from this class"""

    def __init__(self, title, author, genre, year, reading_status):
        self.title = title
        self.author = author
        self.genre = genre
        self.year = year
        self.reading_status = reading_status


class PrintedBook(Book):
    """Classic printed book class"""

    def __init__(self, title, author, genre, year, reading_status, pages):
        super().__init__(title, author, genre, year, reading_status)
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
        owner,
        subscribed,
    ):
        super().__init__(title, author, genre, year, reading_status)
        self.format = eformat
        self.device = device
        self.owner = owner
        self.subscribed = subscribed


class Audiobook(Book):
    """Audiobook class, with few additional parameters related to audiobooks."""

    def __init__(self, title, author, genre, year, reading_status, subscribed):
        super().__init__(title, author, genre, year, reading_status)
        self.subscribed = subscribed
