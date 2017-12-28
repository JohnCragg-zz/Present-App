from unittest import TestCase

from python.src.main.Person import Person
from python.src.main.parser import create_item, create_person
from python.src.main.Item import Item


class TestParser(TestCase):
    def test_can_parse_a_string_into_a_class(self):
        actual = create_person(["ledge@sheg.com", "jonald", "cregg"])
        expected = Person("ledge@sheg.com", "jonald", "cregg")
        self.are_people_equal(actual, expected)

    def test_can_create_item(self):
        actual = create_item(["NotClarkesFresher@warwick.ac.uk", "Coolbrand Bike", 150, 3, "www.bikes.com"])
        expected = Item("NotClarkesFresher@warwick.ac.uk", "Coolbrand Bike", 150, 3, "www.bikes.com")
        self.are_items_equal(actual, expected)

    def are_items_equal(self, actual, expected):
        self.assertEqual(actual.person_email, expected.person_email)
        self.assertEqual(actual.name, expected.name)
        self.assertEqual(actual.price, expected.price)
        self.assertEqual(actual.priority, expected.priority)
        self.assertEqual(actual.hyperlink, expected.hyperlink)

    def are_people_equal(self, actual, expected):
        self.assertEqual(actual.email, expected.email)
        self.assertEqual(actual.first_name, expected.first_name)
        self.assertEqual(actual.last_name, expected.last_name)
