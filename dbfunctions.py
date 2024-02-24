import sqlite3
from sqlite3 import Error
import os
import json


def create_table(conn, table_name):
    """Function to create a table in a database.
    There can be three main types of tables:
    - printed books
    - ebooks
    - audiobooks
    """
    try:
        c = conn.cursor()
        c.execute(f"CREATE TABLE {table_name} (id INTEGER PRIMARY KEY, title TEXT, author TEXT, genre TEXT, year INTEGER, add_date TEXT, pages INTEGER)")

    except Error as e:
        print(e)
        
def delete_table(conn, table_name):
    """Function to delete a table in a database."""
    try:
        c = conn.cursor()
        c.execute(f"DROP TABLE {table_name}")
    except Error as e:
        print(e)
        
def create_connection(database_file):
    """Function to create a connection to a database."""
    conn = None
    try:
        conn = sqlite3.connect(database_file)
    except Error as e:
        print(e)

    return conn

def database_exist(database_file):
    """Function to check if a database file exists.
    Returns True if the database exists, False otherwise."""
    return os.path.exists(database_file)


def add_book_to_database(book, conn, table):
    c = conn.cursor()
    c.execute(f"INSERT INTO {table} VALUES ({book.title}, {book.author}, {book.genre}, {book.year}, {book.add_date}, {book.pages})")

def remove_book_from_database():
    pass


def edit_book_in_database():
    pass


def get_genre_list():
    genres_file = "./genres.txt"
    with open(genres_file, "r") as file:
        genres_list = sorted(file.read().splitlines())
    return genres_list


def get_last_id():
    database_file = "./booksdata.json"
    with open(database_file, "r") as file:
        books_dict = json.load(file)
        id_list = sorted(list(books_dict.keys()))
    return int(id_list[-1])


def show_books():
    database_file = "./booksdata.json"
    with open(database_file, "r") as file:
        books_dict = json.load(file)
        for id, book in books_dict.items():
            print(f"\nBook ID: {id}")
            for key, value in book.items():
                print(f"{key: <10} {value}")


def save_books_to_file():
    database_file = "./booksdata.json"
    with open(database_file, "w", encoding="UTF-8") as file:
        data = json.dumps(books)
        file.write(data)


if __name__ == "__main__":
    print(get_genre_list())
    print()
    print(get_last_id())
    print()
    print(show_books())
