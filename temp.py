import os
from datetime import datetime
import json

file = "./genres.txt"
with open(file, "r") as f:
    genres_list = f.read().splitlines()

for num, genre in enumerate(genres_list, start=1):
    print(num, genre)


books = {}
id = 1
while True:
    os.system("cls")
    title = input("Title: ")
    author = input("Author: ")
    genre = input("Genres: ")
    year = input("Year: ")
    pages = input("Pages: ")
    add_date = datetime.today().date()
    books[str(id)] = {
        "Title:": title,
        "Author:": author,
        "Year:": year,
        "Pages:": pages,
        "Add Date:": str(add_date),
    }
    id += 1
    os.system("cls")
    print(books)
    save_to_file = input("Save books to file?")
    if save_to_file.lower() == "y":
        with open("booksdata.json", "w", encoding="UTF-8") as f:
            data = json.dumps(books)
            f.write(data)

with open("booksdata.json", "r", encoding="UTF-8") as f:
    id = json.loads(f.read())
    print(id)
