from dbfunctions import *
from time import sleep
from menu import MainMenu
from Books import PrintedBook


database_file = "./Data/bookshelf.db"

book = PrintedBook("The Hobbit", "J.R.R. Tolkien", "Fantasy", "1937", "23.02.2024", 153)
def main():
    """Functions that creates main application window and establishes connection to database."""
    create_connection(database_file)


if __name__ == "__main__":
    if database_exist(database_file):
        conn = create_connection(database_file)
        create_table(conn, "PrintedBooks")
        # delete_table(conn, "printedbooks")
        add_book_to_database(book, conn, "PrintedBooks")
        conn.close()

    else:
        print("\nCan't find database file!\n")
        sleep(2)
        exit()
