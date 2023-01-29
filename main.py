from dbfunctions import database_exist_check, create_connection
from settings import *
from time import sleep
from ui_mainscreen import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
from Books import *
from Functionality import add_book
import sys
import pytest
import os


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


def main():
    """Functions that creates main application window and establishes connection to database."""
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    create_connection(database_file)
    sys.exit(app.exec())


if __name__ == "__main__":
    if database_exist_check(database_file):
        # ksiazka = PrintedBook(
        #     "Opowieści Pilota Pirxa",
        #     "Stanisław Lem",
        #     "Science Fiction",
        #     1965,
        #     False,
        #     219,
        # )
        # eksiazka = EBook(
        #     "Hyperion",
        #     "Dan Simmons",
        #     "Science Fiction",
        #     1989,
        #     True,
        #     "mobi",
        #     "Kindle",
        #     "Sebastian Kupis",
        #     False,
        # )
        # audioksiazka = Audiobook(
        #     "Python3 Object-Oriented Programming",
        #     "Dusty Philips",
        #     "Education",
        #     2018,
        #     True,
        #     False,
        # )

        # print(ksiazka.title)
        # print(ksiazka.pages)
        # print(eksiazka.device)
        # print(eksiazka.author)
        # print(audioksiazka.author)
        # print(audioksiazka.year)

        add_book()

    else:
        print("\nCan't find database file!\n")
        sleep(1)
        exit()
