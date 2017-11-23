from python.src.main.Person import Person


class Parser(object):
    def __init__(self, string_to_parse):
        self.string_to_parse = string_to_parse

    def create_person(self):
        (first_name, second_name, age, description) = self.string_to_parse.split(",")
        return Person(first_name, second_name, int(age), description)
