import db
import sqlite3


def main():
    conn = sqlite3.connect("person_and_item.db")
    cursor = conn.cursor()

    db.create_person_table(cursor)
    db.create_item_table(cursor)
    cregg = Person("ledge@sheg.com", "jonald", "cregg")
    cregg.say_hello()

    print("marks a bellend")


if __name__ == '__main__': main()
