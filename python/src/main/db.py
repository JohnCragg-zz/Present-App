import sqlite3
from sqlite3 import Error
from python.src.main.Person import Person
from python.src.main.Item import Item
from python.src.main.parser import Parser

mark = Person('SparkyMark123@grinder.com', "Mark", "Holmes")
john = Person("FredSaidIWasBoring@loser.com", "John", "Cragg")
clarke = Person("NotClarkesFresher@warwick.ac.uk", "Clarke", "Clarkson")
people_mark_cares_about = [mark, john, clarke]

bike = Item("NotClarkesFresher@warwick.ac.uk", 'Coolbrand Bike', 150, 3, 'www.bikes.com')
ps2 = Item("NotClarkesFresher@warwick.ac.uk", 'Playstation 2', 60, 4, 'www.game.com')
bs = Item("NotClarkesFresher@warwick.ac.uk", 'Banana Suit', 55, 1, 'wwww.clerksfresh.org')
banter = Item("FredSaidIWasABoring@loser.com", "Bants", 50000, 1, 'www.sportyjake.com')
copas = Item("FredSaidIWasABoring@loser.com", "Copa Mundials", 90, 2, 'www.jjb.co.uk')
clarkes_xmas_list = [bike, ps2, bs]
creggs_xmas_list = [banter, copas]


def create_person_table(c):
    c.execute(
        "CREATE TABLE IF NOT EXISTS Person(email TEXT PRIMARY KEY, first_name TEXT, last_name TEXT)"
    )


def create_item_table(c):
    c.execute(
        "CREATE TABLE IF NOT EXISTS Item(person_email TEXT, name TEXT, price REAL, priority INT, hyperlink TEXT)"
    )


def insert_person(c, conn, person):
    c.execute("INSERT INTO Person VALUES('%s', '%s', '%s')"
              % (person.email, person.first_name, person.last_name))
    conn.commit()


def insert_item(c, conn, item):
    c.execute("INSERT INTO Item VALUES('%s', '%s', '%d', '%d', '%s')"
              % (item.person_email, item.name, item.price, item.priority, item.hyperlink))
    conn.commit()


def populate_table(lst, conn, c, insert_method):
    for element in lst:
        insert_method(c, conn, element)
        print("Inserted element, %s, into the database" % element)

def read_table(c, title):
    if title == Person:
        c.execute("SELECT * FROM Person")
        for row in c:
            print(row)
    elif title == Item:
        c.execute("SELECT * FROM Item")
        for row in c:
           print(row)
    else:
        print("Table not found.")

def get_persons_items(c, email):
    c.execute("SELECT * FROM Item WHERE person_email = '%s'" % email)
    for row in c:
        print(row)

def create_item_from_table(c, email):
    c.execute("SELECT * FROM Item WHERE person_email = '%s'" % email)
    list_of_items = []
    for row in c:
        item_from_row = Parser(str(row)).create_item()
        list_of_items.append(item_from_row)
    for obj in list_of_items:
        print(obj.name)

if __name__ == '__main__':
    try:
        conn = sqlite3.connect("person_and_item.db")
        cursor = conn.cursor()

        create_person_table(cursor)
        create_item_table(cursor)

        #populate_table(people_mark_cares_about, conn, cursor, insert_person)
        #populate_table(clarkes_xmas_list, conn, cursor, insert_item)
        #populate_table(creggs_xmas_list, conn, cursor, insert_item)


        #read_table(cursor, Person)
        #read_table(cursor, Item)

        get_persons_items(cursor, "NotClarkesFresher@warwick.ac.uk")
        create_item_from_table(cursor, "NotClarkesFresher@warwick.ac.uk")
    except Error as e:
        print(e)
    finally:
        conn.close()
