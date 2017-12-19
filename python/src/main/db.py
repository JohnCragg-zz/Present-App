import sqlite3
from sqlite3 import Error
from python.src.main.Person import Person
from python.src.main.Item import Item

mark = Person(1, 'SparkyMark123@grinder.com', "Mark", "Holmes")
john = Person(2, "FredSaidIWasBoring@loser.com", "John", "Cragg")
clarke = Person(3, "NotClakersFresher@warwick.ac.uk", "Clarke", "Clarkson")
people_mark_cares_about = [mark, john, clarke]

bike = Item(3, 'Coolbrand Bike', 150, 3, 'www.bikes.com')
ps2 = Item(3, 'Playstation 2', 60, 4, 'www.game.com')
bs = Item(3, 'Banana Suit', 55, 1, 'wwww.clerksfresh.org')
clarkes_xmas_list = [bike, ps2, bs]


def create_person_table(c):
    c.execute(
        "CREATE TABLE IF NOT EXISTS Person(personal_id INT, email TEXT, first_name TEXT, last_name TEXT)"
    )


def create_item_table(c):
    c.execute(
        "CREATE TABLE IF NOT EXISTS Item(person_id INT, name TEXT, price REAL, priority INT, hyperlink TEXT)"
    )


def insert_person(c, conn, person):
    c.execute("INSERT INTO Person VALUES('%d', '%s', '%s', '%s')"
              % (person.personal_id, person.email, person.first_name, person.last_name))
    conn.commit()


def insert_item(c, conn, item):
    c.execute("INSERT INTO Item VALUES('%d', '%s', '%d', '%d', '%s')"
              % (item.person_id, item.name, item.price, item.priority, item.hyperlink))
    conn.commit()


def populate_table(lst, conn, c, insert_method):
    for element in lst:
        insert_method(c, conn, element)
        print("Inserted element, %s, into the database" % element)
    c.close()


def create_connection():
    c = conn.cursor()
    create_person_table(c)
    create_item_table(c)

    populate_table(people_mark_cares_about, conn, c, insert_person)
    populate_table(clarkes_xmas_list, conn, c, insert_item)
    return c


def read_person_table(c):
    c.execute("SELECT * FROM Person")
    for row in c:
        print(row)


def read_item_table(c):
    c.execute("SELECT * FROM Item")
    for row in c:
        print(row)


if __name__ == '__main__':
    try:
        conn = sqlite3.connect("person_and_item.db")
        cursor = create_connection()
        read_person_table(cursor)
        read_item_table(cursor)
    except Error as e:
        print(e)
    finally:
        conn.close()
