from dbfunctions import get_last_id

last_id = get_last_id()


class Book:
    """Main Book class, other classes will inherit from this class"""

    def __init__(
        self,
        title: str,
        author: str,
        genre: str,
        year: int,
        add_date: str,
    ):
        self.title = title
        self.author = author
        self.genre = genre
        self.year = year
        self.add_date = add_date
        global last_id
        last_id += 1
        self.id = last_id


class PrintedBook(Book):
    """Classic printed book class"""

    def __init__(
        self,
        title: str,
        author: str,
        genre: str,
        year: int,
        add_date: str,
        pages,
    ):
        super().__init__(
            title,
            author,
            genre,
            year,
            add_date,
        )
        self.pages = pages


class EBook(Book):
    """Ebook class, with few additional parameters related to ebooks."""

    def __init__(
        self,
        title: str,
        author: str,
        genre: str,
        year: int,
        add_date: str,
        eformat,
        device,
    ):
        super().__init__(
            title,
            author,
            genre,
            year,
            add_date,
        )
        self.format = eformat
        self.device = device


class Audiobook(Book):
    """Audiobook class, with few additional parameters related to audiobooks."""

    def __init__(
        self,
        title: str,
        author: str,
        genre: str,
        year: int,
        add_date: str,
        subscribed,
    ):
        super().__init__(
            title,
            author,
            genre,
            year,
            add_date,
        )
        self.subscribed = subscribed
