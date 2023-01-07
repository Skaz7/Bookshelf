import os
import sqlite3
from settings import *


def database_exist_check():
    return os.path.exists(DB_FILE_NAME)


def connect_to_database():
    conn = sqlite3.connect(DB_FILE_NAME)
    cursor = conn.cursor()
