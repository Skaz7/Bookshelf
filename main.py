from dbfunctions import database_exist_check
from time import sleep
from menu import MainMenu


database_file = "./Data/bookshelf.db"

books_dict = {}


def main():
    """Functions that creates main application window and establishes connection to database."""
    create_connection(database_file)


if __name__ == "__main__":
    if database_exist_check(database_file):
        MainMenu().run()

    else:
        print("\nCan't find database file!\n")
        sleep(1)
        exit()
