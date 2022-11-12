import os
import sqlite3
from datetime import datetime


DB_FILE_NAME = './Data/bookshelf.db'


def database_exist_check():
    return os.path.exists(DB_FILE_NAME)


def connect_to_database():
    conn = sqlite3.connect(DB_FILE_NAME)
    cursor = conn.cursor()


class Book:
    def __init__(self, title, author, genre, year, reading):
        self.title = title
        self.author = author
        self.genre = genre
        self.year = year
        self.reading = reading


class PrintedBook(Book):
    def __init__(self, title, author, genre, year, reading, pages):
        super().__init__(self, title, author, genre, year, reading)
        self.pages = pages


class EBook(Book):
    def __init__(self, title, author, genre, year, reading, eformat, device, owner, subscribed):
        super().__init__(self, title, author, genre, year, reading)
        self.format = eformat
        self.device = device
        self.owner = owner
        self.subscribed = subscribed


class Audiobook(Book):
    def __init__(self, title, author, genre, year, reading, subscribed):
        super().__init__(self, title, author, genre, year, reading)
        self.subscribed = subscribed


class Owner:
    def __init__(self, firstname: str, lastname: str, borrowdate: str, returned: bool, returndate: str):
        self.firstname = firstname
        self.lastname = lastname
        self.borrowdate = borrowdate
        self.returned = returned
        self.returndate = returndate

    def borrowtime(self):
        borrowtime = datetime.strptime(self.returndate, "%Y-%M-%d") - datetime.strptime(self.borrowdate, "%Y-%M-%d")
        return f"You have this book borrowed for {borrowtime}."


class Read:
    def __init__(self, start, end, duringreading, note, review):
        self.start = start
        self.end = end
        self.duringreading = duringreading
        self.note = note
        self.review = review
