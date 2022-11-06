import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def select_all_customers(conn):
    cur = conn.cursor()
    # cur.execute("DELETE FROM customers WHERE CustomerId='60'")

    def add_record():
        cur.execute("INSERT INTO customers VALUES('60', 'Jimi', 'Hendrix', '', 'Gimnazjalna 44A', 'Wrocław', '',"
                    " 'Poland', '51170', '+48796589150', '', 'jimi.hendrix@gmail.com', '3')")

    add_record()

    cur.execute("SELECT * FROM customers")

    rows = cur.fetchall()

    for row in rows:
        print(row)


def main():
    database = "chinook.db"

    conn = create_connection(database)

    with conn:
        print("\n1. Customers\n")
        select_all_customers(conn)


if __name__ == '__main__':
    main()
