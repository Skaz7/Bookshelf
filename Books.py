last_id = 0


class Book:
    """Main Book class, other classes will inherit from this class"""

    def __init__(
        self,
        title,
        author,
        genre,
        year,
        add_date,
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
        title,
        author,
        genre,
        year,
        add_date,
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
        title,
        author,
        genre,
        year,
        add_date,
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
        title,
        author,
        genre,
        year,
        add_date,
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
