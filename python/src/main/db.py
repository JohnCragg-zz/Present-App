import logging
from sqlite3 import IntegrityError


class DB(object):
    def __init__(self, cursor, conn):
        self.cursor = cursor
        self.conn = conn
        conn.text_factory = str

    def create_person_table(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS Person(email TEXT PRIMARY KEY, first_name TEXT, last_name TEXT)"
        )
        logging.info("Person table created")

    def create_item_table(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS Item(person_email TEXT, name TEXT, price REAL, priority INT, hyperlink TEXT)"
        )
        logging.info("Item table created")

    def insert_person(self, person):
        try:
            print(person.email)
            self.cursor.execute("INSERT INTO Person VALUES('%s', '%s', '%s')"
                                % (person.email, person.first_name, person.last_name))
            self.conn.commit()
        except IntegrityError:
            logging.error("Key '%s' was not unique and hasn't been entered into the db" % person.email)

    def insert_item(self, item):
        self.cursor.execute("INSERT INTO Item VALUES('%s', '%s', '%s', '%d', '%s')"
                            % (item.person_email, item.name, item.price, item.priority, item.hyperlink))
        self.conn.commit()

    def populate_table(self, lst, insert_method):
        for element in lst:
            insert_method(element)
            logging.info("Inserted element, %s, into the database" % element)

    def get_items(self, email):
        items = []
        rows = self.cursor.execute("SELECT * FROM Item WHERE person_email = '%s'" % email)
        for row in rows:
            items += row
        return items

    def get_item(self, email, name):
        items = []
        rows = self.cursor.execute("SELECT * FROM ITEM WHERE person_email = '%s' AND name = '%s'"
                            % (email, name))
        for row in rows:
            items += row
        return items

    def get_person(self, email):
        person = []
        rows = self.cursor.execute("SELECT * FROM Person WHERE email = '%s'" % email)
        for row in rows:
            person += row
        return person

    def delete_person(self, email):
        self.cursor.execute("DELETE FROM Person WHERE email = '%s'" % email)
        self.cursor.execute("DELETE FROM Item WHERE person_email = '%s" % email)
        self.conn.commit()

    def delete_all_persons_items(self, person_email):
        self.cursor.execute("DELETE FROM Item WHERE person_email = '%s'"
                            % person_email)
        self.conn.commit()

    def delete_item(self, person_email, name):
        self.cursor.execute("DELETE FROM Item WHERE person_email = '%s' AND name = '%s'"
                            % (person_email, name))
        self.conn.commit()


