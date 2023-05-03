from dbfunctions import database_exist_check, create_connection
from time import sleep
from menu import MainMenu


database_file = "./Data/bookshelf.db"


def main():
    """Functions that creates main application window and establishes connection to database."""
    create_connection(database_file)


if __name__ == "__main__":
    if database_exist_check(database_file):
        MainMenu().run()

    else:
        print("\nCan't find database file!\n")
        sleep(2)
        exit()
