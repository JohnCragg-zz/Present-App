from unittest import TestCase

from python.src.main.Person import Person
from python.src.main.parser import Parser


class TestParser(TestCase):
    def setUp(self):
        self.parser = Parser("mark,holmes,23,bellend")

    def test_can_parse_a_string_into_a_class(self):
        actual = self.parser.create_person()
        expected = Person("mark", "holmes", 23, "bellend")
        self.assertEqual(actual.first_name, expected.first_name)
        self.assertEqual(actual.second_name, expected.second_name)
        self.assertEqual(actual.age, expected.age)
        self.assertEqual(actual.description, expected.description)

print("herpy derp")
