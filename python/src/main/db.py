from python.src.main.Item import Item
from python.src.main.Person import Person
from python.src.main.parser import Parser


class DB(object):
    def __init__(self, cursor, conn):
        self.cursor = cursor
        self.conn = conn
        conn.text_factory = str

    def create_person_table(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS Person(email TEXT PRIMARY KEY, first_name TEXT, last_name TEXT)"
        )

    def create_item_table(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS Item(person_email TEXT, name TEXT, price REAL, priority INT, hyperlink TEXT)"
        )

    def insert_person(self, person):
        self.cursor.execute("INSERT INTO Person VALUES('%s', '%s', '%s')"
                            % (person.email, person.first_name, person.last_name))
        self.conn.commit()

    def insert_item(self, item):
        self.cursor.execute("INSERT INTO Item VALUES('%s', '%s', '%d', '%d', '%s')"
                            % (item.person_email, item.name, item.price, item.priority, item.hyperlink))
        self.conn.commit()

    def populate_table(self, lst, insert_method):
        for element in lst:
            insert_method(element)
            print("Inserted element, %s, into the database" % element)

    def read_table(self, title):
        if title == Person:
            self.cursor.execute("SELECT * FROM Person")
            for row in self.cursor:
                print(row)
        elif title == Item:
            self.cursor.execute("SELECT * FROM Item")
            for row in self.cursor:
                print(row)
        else:
            print("Table not found.")

    def get_persons_items(self, email):
        return self.cursor.execute("SELECT * FROM Item WHERE person_email = '%s'" % email)

    def create_item_from_table(self, email):
        self.cursor.execute("SELECT * FROM Item WHERE person_email = '%s'" % email)
        items = []
        for row in self.cursor:
            item = Parser(row).create_item()
            items.append(item)
        return items
