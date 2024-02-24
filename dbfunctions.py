import sqlite3
from sqlite3 import Error
import os


def create_table(conn, table_name):
    """Function to create a table in a database.
    There can be three main types of tables:
    - printed books
    - ebooks
    - audiobooks
    """
    try:
        c = conn.cursor()
        c.execute(
            f"CREATE TABLE {table_name} (id INTEGER PRIMARY KEY, title TEXT, author TEXT, genre TEXT, year INTEGER, add_date TEXT, pages INTEGER)"
        )

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


def add_book_to_database(conn, book, table):
    c = conn.cursor()

    try:
        c.execute(
            f"INSERT INTO {table} VALUES (NULL, '{book.title}', '{book.author}', '{book.genre}', {book.year}, '{book.add_date}', {book.pages})"
        )
    except Error as e:
        print(e)

    conn.commit()


def remove_book_from_database(conn, title, author, table):
    c = conn.cursor()

    try:
        c.execute(
            f"DELETE FROM {table} WHERE title = '{title}' AND author = '{author}'"
        )
    except Error as e:
        print(e)

    conn.commit()


def edit_book_in_database():
    pass


def get_genre_list():
    genres_file = "./genres.txt"
    with open(genres_file, "r") as file:
        genres_list = sorted(file.read().splitlines())
    return genres_list


def show_books(conn):
    c = conn.cursor()
    c.execute("SELECT * FROM PrintedBooks")
    rows = c.fetchall()
    for row in rows:
        print(row)
