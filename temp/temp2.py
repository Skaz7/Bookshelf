import sqlite3


DATABASE_FILE = './Data/bookshelf.db'

db_connection = sqlite3.connect(DATABASE_FILE)
db_cursor = db_connection.cursor()
db_cursor.execute("CREATE TABLE printedbooks (id INTEGER PRIMARY KEY, title TEXT, author TEXT, genre TEXT, year INTEGER, add_date TEXT, pages INTEGER)")
books = db_cursor.fetchall()
print(books)
db_connection.close()
