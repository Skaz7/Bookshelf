from Books import Book, PrintedBook, EBook, Audiobook
from datetime import datetime
import os


database_file = "./Data/bookshelf.db"


class Catalog:
    """Main class for storing and searching for books.
    User can search database by book type (printed, ebook, audiobook), by author name,
    by genre, by owner, and by country."""

    def __init__(self):
        """Initialize catalogue with an empty list of books."""
        self.books = []

    def new_book(self):
        """Create a new book with the given information."""

        print("Adding new book to library:")
        title = input("Book Title: ")
        author = input("Book Author: ")
        genre = input("Book Genre: ")
        year = input("Book Year: ")
        add_date = datetime.today().date()

        new_book = Book(title, author, genre, year, add_date)
        self.books.append(new_book)

        print("\nBook added to library!\n")
        print(f"Title  - {new_book.title}")
        print(f"Author - {new_book.author}")
        print(f"Genre  - {new_book.genre}")
        print(f"Year   - {new_book.year}")
        print(f"Added  - {new_book.add_date}")
        input()

    # def new_printed_book(self, title, author, genre, year, pages):
    #     """Create a new printed book with the given information."""
    #     self.books.append(PrintedBook(title, author, genre, year, pages))

    # def new_ebook(self, title, author, genre, year, eformat, device):
    #     """Create a new ebook with the given information."""
    #     self.books.append(EBook(title, author, genre, year, eformat, device))

    # def new_Audiobook(self, title, author, genre, year, subscribed):
    #     """Create a new Audiobook with the given information."""
    #     self.books.append(Audiobook(title, author, genre, year, subscribed))

    def delete_book(
        self,
    ):
        pass

    def edit_book(
        self,
    ):
        pass
