from dbfunctions import database_exist_check, create_connection
from settings import *
from time import sleep
from Books import *
from Functionality import add_book
import sys
import pytest
import os


def main():
    """Functions that creates main application window and establishes connection to database."""
    create_connection(database_file)


if __name__ == "__main__":
    if database_exist_check(database_file):
        add_book()

    else:
        print("\nCan't find database file!\n")
        sleep(1)
        exit()
