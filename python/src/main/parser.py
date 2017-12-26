from python.src.main.Person import Person
from python.src.main.Item import Item


class Parser(object):
    def __init__(self, row):
        self.row = row

    def create_person(self):
        (email, first_name, last_name) = self.row[0], self.row[1], self.row[2]
        return Person(email, first_name, last_name)

    def create_item(self):
        person_email, name, price, priority, hyperlink = self.row[0], self.row[1], self.row[2], self.row[3], self.row[4]
        return Item(person_email, name, price, priority, hyperlink)
