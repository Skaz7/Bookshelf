from Books import Book, PrintedBook, EBook, Audiobook
from datetime import datetime
import time


database_file = "./Data/bookshelf.db"


class Catalog:
    """Main class for storing and searching for books.
    User can search database by book type (printed, ebook, audiobook), by author name,
    by genre, by owner, and by country."""

    def __init__(self):
        """Initialize catalogue with an empty list of books."""
        self.books = []

    def add_book(self, new_book):
        self.books.append(new_book)

    def delete_book(
        self,
    ):
        pass

    def edit_book_info(
        self,
    ):
        pass
