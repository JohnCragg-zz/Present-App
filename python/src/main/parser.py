from python.src.main.Person import Person


class Parser(object):
    def __init__(self, string_to_parse):
        self.string_to_parse = string_to_parse

    def create_person(self):
        (personal_id, email, first_name, second_name) = self.string_to_parse.split(",")
        return Person(personal_id, email, first_name, second_name)
