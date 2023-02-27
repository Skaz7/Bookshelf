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
    pages = int(input("Book pages: "))

    new_book = PrintedBook(
        title=title,
        author=author,
        genre=genre,
        year=year,
        add_date=datetime.today().date(),
        pages=pages,
    )

    print("\n\nBook created!\n")
    print(f"Title:     {new_book.title}")
    print(f"Author:    {new_book.author}")
    print(f"Genre:     {new_book.genre}")
    print(f"Year:      {new_book.year}")
    print(f"Pages:     {new_book.pages}")
    print(f"Added:     {new_book.add_date}\n")
    print("\nAdd this book to database (Y/N) ?\n")
