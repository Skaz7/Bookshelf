from datetime import datetime
from Books import Book, PrintedBook, EBook, Audiobook


database_file = "./Data/bookshelf.db"


class Catalogue:
    """Main class for storing and searching for books.
    User can search database by book type (printed, ebook, audiobook), by author name,
    by genre, by owner, and by country."""

    def __init__(self):
        """Initialize catalogue with an empty list of books."""
        self.books = []

    def new_printed_book(self, title, author, genre, year, pages):
        """Create a new printed book with the given information."""
        self.books.append(PrintedBook(title, author, genre, year, pages))

    def new_ebook(self, title, author, genre, year, eformat, device):
        """Create a new ebook with the given information."""
        self.books.append(EBook(title, author, genre, year, eformat, device))

    def new_Audiobook(self, title, author, genre, year, subscribed):
        """Create a new Audiobook with the given information."""
        self.books.append(Audiobook(title, author, genre, year, subscribed))


class Owner:
    """Owner class with information about borrowed books."""

    def __init__(
        self,
        firstname: str,
        lastname: str,
        borrowdate: str,
        returned: bool,
        returndate: str,
    ):
        self.firstname = firstname
        self.lastname = lastname
        self.borrowdate = borrowdate
        self.returned = returned
        self.returndate = returndate

    def borrowtime(self):
        borrowtime = datetime.strptime(self.returndate, "%Y-%M-%d") - datetime.strptime(
            self.borrowdate, "%Y-%M-%d"
        )
        return f"You have this book borrowed for {borrowtime}."


class Read:
    """Read class with information about reading a book."""

    def __init__(self, start, end, duringreading, note, review):
        self.start = start
        self.end = end
        self.duringreading = duringreading
        self.note = note
        self.review = review
