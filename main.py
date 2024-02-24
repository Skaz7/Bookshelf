from dbfunctions import *
from time import sleep
from menu import MainMenu
from Books import PrintedBook


database_file = "./Data/bookshelf.db"
menu = MainMenu()


def main():
    """Functions that creates main application window and establishes connection to database."""
    create_connection(database_file)


if __name__ == "__main__":
    if database_exist(database_file):
        menu.run()

    else:
        print("\nCan't find database file!\n")
        sleep(2)
        exit()
