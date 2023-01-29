import os
import sqlite3
from settings import *
from Books import *


def database_exist_check(DB_FILE_NAME):
    return os.path.exists(DB_FILE_NAME)


def connect_to_database(DB_FILE_NAME):
    conn = sqlite3.connect(DB_FILE_NAME)
    cursor = conn.cursor()


def add_book():
    os.system("cls")
    print("Adding book\n")
    title = input("Book title: ")
    author = input("Book author: ")
    genre = input("Book genre: ")
    year = int(input("Book year: "))
    reading_status = bool(input("Book reading status: "))
    pages = int(input("Book pages: "))

    new_book = PrintedBook(title, author, genre, year, reading_status, pages)

    print("Book created!")
    print(new_book.title)
    print(new_book.author)
    print(new_book.genre)
    print(new_book.year)
    print(new_book.reading_status)
    print(new_book.pages)
    print("\nAdd this book to database (Y/N) ?")
