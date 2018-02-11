from python.src.main.Person import Person
from python.src.main.Item import Item


def create_person(row):
    (email, first_name, last_name) = row[0], row[1], row[2]
    return Person(email, first_name, last_name)


def create_item(row):
    person_email, name, price, priority, hyperlink = row[0], row[1], row[2], row[3], row[4]
    return Item(person_email, name, price, priority, hyperlink)

def parse_list_of_items(lst):
    for i in range(0, len(lst), 5):
        yield lst[i: i+5]