from dbfunctions import *
from time import sleep
from menu import MainMenu
from Books import PrintedBook


database_file = "./Data/bookshelf.db"

book1 = PrintedBook("The Hobbit", "J.R.R. Tolkien", "Fantasy", 1937, "23.02.2024", 153)
book2 = PrintedBook(
    "The Lord of the Rings", "J.R.R. Tolkien", "Fantasy", 1954, "24.02.2024", 1178
)


def main():
    """Functions that creates main application window and establishes connection to database."""
    create_connection(database_file)


if __name__ == "__main__":
    if database_exist(database_file):
        conn = create_connection(database_file)
        create_table(conn, "PrintedBooks")
        # delete_table(conn, "PrintedBooks")
        add_book_to_database(conn, book1, "PrintedBooks")
        add_book_to_database(conn, book2, "PrintedBooks")
        input()
        remove_book_from_database(conn, book1, "PrintedBooks")
        conn.close()

    else:
        print("\nCan't find database file!\n")
        sleep(2)
        exit()
