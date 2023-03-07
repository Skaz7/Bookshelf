import sys
import os
from catalog import Catalog
import time
from Functionality import add_book


class MainMenu:
    """Displays menu and responds to choices when run."""

    def __init__(self):
        self.catalog = Catalog()
        self.choices = {
            "1": self.show_books,
            "2": self.search_books,
            "3": self.add_book,
            "4": self.edit_book,
            "0": self.quit,
        }

    def display_menu(self):
        os.system("cls")
        print(
            """
Catalogue Menu:

    1. Show Books
    2. Search for book
    3. Add new book
    4. Edit book info

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

    def show_books(self):
        pass

    def search_books(self):
        pass

    def add_book(self):
        add_book()

    def edit_book(self):
        pass

    def quit(self):
        quit()


menu = MainMenu()
menu.run()
