import os
from dbfunctions import *
import time
from datetime import datetime
from Books import PrintedBook


database_file = "./Data/bookshelf.db"


class MainMenu:
    """Displays menu and responds to choices when run."""

    def __init__(self):
        self.choices = {
            "1": self.show_bookshelf,
            "2": self.search_books,
            "3": self.new_printed_book,
            "4": self.edit_book,
            "5": self.delete_book,
            "0": self.quit,
        }

    def display_menu(self):
        os.system("cls")
        print(
            """

    1. Show Books
    2. Search for book
    3. Add new book
    4. Edit book info
    5. Delete book

    0. QUIT
"""
        )

    def run(self):
        """Displays the menu and responds to choices."""
        while True:
            self.display_menu()
            choice = input("Enter an option: >  ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print(f"{choice} is not a valid option.")
                time.sleep(1)

    def show_bookshelf(self):
        books = self.catalog.books
        print(books)
        input()

    def search_books(self):
        """Searches book Catalog for a book with the given title."""
        print("Searching for book in library:")
        title = input("Book Title: ").title()
        print(show_books(title))
        time.sleep(2)
        return

    def new_printed_book(self):
        """Create a new book with the given information."""
        print("Adding new book to library:")

        title = input("Book Title: ").title()
        author = input("Book Author: ").title()
        genre = input("Book Genre: ").title()
        year = input("Book Year: ")
        add_date = datetime.today().date()
        pages = input("Number of Pages: ")

        new_book = PrintedBook(title, author, genre, year, add_date, pages)

        while True:
            choice = input("\nAdd this book to the Library? (Y/N)  > \n").lower()
            if choice == "y" or choice == "yes":
                conn = create_connection(database_file)
                add_book_to_database(conn, new_book, "PrintedBooks")
                conn.close()
                print("Book added to library.")
                time.sleep(2)
                return

            elif choice == "n" or choice == "no":
                print("Book not added.")
                time.sleep(2)
                return

            else:
                print("Invalid input.")
                time.sleep(2)

    def edit_book(self):
        pass

    def delete_book(self):
        pass

    def quit(self):
        print("\nThank you for using Bookshelf. Goodbye.\n")
        time.sleep(1)
        quit()
