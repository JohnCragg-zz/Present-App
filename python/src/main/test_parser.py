from unittest import TestCase
from main import *


class TestParser(TestCase):
    def setUp(self):
        self.parser = Parser("mark,holmes,23,bellend")

    def test_can_parse_a_string_into_a_class(self):
        actual = parser.create_person()
        expected = Person("mark", "holmes", 23, "bellend")
        assertEqual(actual, expected)
