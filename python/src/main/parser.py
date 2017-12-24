from python.src.main.Person import Person
from python.src.main.Item   import Item

class Parser(object):
    def __init__(self, string_to_parse):
        self.string_to_parse = string_to_parse

    def create_person(self):
        (email, first_name, last_name) = self.string_to_parse.split(",")
        return Person(email, first_name, last_name)

    def create_item(self):
        (person_email, name, price, priority, hyperlink) = self.string_to_parse.split(",")
        return Item(person_email, name, price, priority, hyperlink)


