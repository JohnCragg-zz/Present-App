class Parser(object):
    def __init__(self, string_to_parse):
        self.string_to_parse = string_to_parse

    def create_person(self):
        thing = self.string_to_parse.split(",")
        self.Person = Person(thing[0],thing[1],thing[2],thing[3])
