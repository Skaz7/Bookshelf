class Book:
    """Main Book class, other classes will inherit from this class"""
    def __init__(self, title, author, genre, year, reading):
        self.title = title
        self.author = author
        self.genre = genre
        self.year = year
        self.reading = reading


class PrintedBook(Book):
    """Classic printed book class"""
    def __init__(self, title, author, genre, year, reading, pages):
        super().__init__(self, title, author, genre, year, reading)
        self.pages = pages


class EBook(Book):
    """Ebook class, with few additional parameters related to ebooks."""
    def __init__(self, title, author, genre, year, reading, eformat, device, owner, subscribed):
        super().__init__(self, title, author, genre, year, reading)
        self.format = eformat
        self.device = device
        self.owner = owner
        self.subscribed = subscribed


class Audiobook(Book):
    """Audiobook class, with few additional parameters related to audiobooks."""
    def __init__(self, title, author, genre, year, reading, subscribed):
        super().__init__(self, title, author, genre, year, reading)
        self.subscribed = subscribed