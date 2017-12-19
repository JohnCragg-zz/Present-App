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

# 'create' methods

def create_person_table(c):
    c.execute(
        "CREATE TABLE IF NOT EXISTS Person(personal_id INT, email TEXT, first_name TEXT, last_name TEXT)"
    )

def create_item_table(c):
    c.execute(
        "CREATE TABLE IF NOT EXISTS Item(person_id INT, name TEXT, price REAL, priority INT, hyperlink TEXT)"
    )

# 'insert' methods

def insert_person(c, conn, person):
    c.execute("INSERT INTO Person VALUES('%d', '%s', '%s', '%s')"
              % (person.personal_id, person.email, person.first_name, person.last_name))
    conn.commit()

def insert_item(c, conn, item):
    c.execute("INSERT INTO Item VALUES('%d', '%s', '%d', '%d', '%s')"
              % (item.person_id, item.name, item.price, item.priority, item.hyperlink))
    conn.commit()

# 'create connection' methods

def create_connection_person(db_file):
    try:
        conn = sqlite3.connect(db_file)
        c = conn.cursor()
        create_person_table(c)

        for person in people_mark_cares_about:
           insert_person(c, conn, person)
           print("Inserted person, %s, into the database" % person.first_name)

        c.close()
        print("populated table")

    except Error as e:
        print(e)
    finally:
        conn.close()

def create_connection_item(db_file):
    try:
        conn = sqlite3.connect(db_file)
        c = conn.cursor()
        create_item_table(c)

        for item in clarkes_xmas_list:
            insert_item(c, conn, item)
            print("Inserted item, %s, into the database" % item.name)

        c.close()
        print("populated table")

    except Error as e:
        print(e)
    finally:
        conn.close()

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        c = conn.cursor()
        d = conn.cursor()
        create_person_table(c)
        create_item_table(d)

        for person in people_mark_cares_about:
           insert_person(c, conn, person)
           print("Inserted person, %s, into the database" % person.first_name)

        c.close()
        print("populated table")

        for item in clarkes_xmas_list:
            insert_item(d, conn, item)
            print("Inserted item, %s, into the database" % item.name)

        d.close()
        print("populated table")

    except Error as e:
        print(e)
    finally:
        conn.close()

if __name__ == '__main__':
#    create_connection_person("person.db")
#    create_connection_item("item.db")
    create_connection("person_and_item.db")

def read_person_table(db_file):
    try:
        conn = sqlite3.connect(db_file)
        c = conn.cursor()

        c.execute("SELECT * FROM Person")
        for row in c:
            print(row)

    except Error as e:
        print(e)
    finally:
        conn.close()

def read_item_table(db_file):
    try:
        conn = sqlite3.connect(db_file)
        c = conn.cursor()

        c.execute("SELECT * FROM Item")
        for row in c:
            print(row)

    except Error as e:
        print(e)
    finally:
        conn.close()

read_person_table("person_and_item.db")
read_item_table("person_and_item.db")

