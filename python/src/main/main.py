import db
import sqlite3


def main():
    conn = sqlite3.connect("person_and_item.db")
    cursor = conn.cursor()

    db.create_person_table(cursor)
    db.create_item_table(cursor)


if __name__ == '__main__':
    main()