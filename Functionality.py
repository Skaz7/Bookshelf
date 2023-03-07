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

    book = PrintedBook(
        title=title,
        author=author,
        genre=genre,
        year=year,
        add_date=datetime.today().date(),
        pages=pages,
    )

    print("\n\nBook created!\n")
    print(f"ID:        {book.id}")
    print(f"Title:     {book.title}")
    print(f"Author:    {book.author}")
    print(f"Genre:     {book.genre}")
    print(f"Year:      {book.year}")
    print(f"Pages:     {book.pages}")
    print(f"Added:     {book.add_date}\n")
    print("\nAdd this book to database (Y/N) ?\n")
    choice = input()

    if choice.lower() == "y" or choice.lower() == "yes":
        return book
    elif choice.lower() == "n" or choice.lower() == "no":
        pass
    else:
        print("Please enter a valid choice (Y/N)")


def print_book_data():
    print(f"ID:        {book.id}")
    print(f"Title:     {book.title}")
    print(f"Author:    {book.author}")
    print(f"Genre:     {book.genre}")
    print(f"Year:      {book.year}")
    print(f"Pages:     {book.pages}")
    print(f"Added:     {book.add_date}\n")


def print_all_books_titles():
    pass
