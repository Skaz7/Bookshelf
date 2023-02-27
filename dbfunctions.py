import sqlite3
from sqlite3 import Error
import os


def create_connection(db_file):
    """Function to create a connection to a database."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def database_exist_check(database_file):
    """Function to check if a database file exists.
    Returns True if the database exists, False otherwise."""
    return os.path.exists(database_file)


def add_book_to_database():
    pass


def remove_book_from_database():
    pass


def edit_book_in_database():
    pass
