from unittest import TestCase

from python.src.main.Person import Person
from python.src.main.parser import Parser


class TestParser(TestCase):
    def setUp(self):
        self.parser = Parser("1,ledge@sheg.com,jonald,cregg")

    def test_can_parse_a_string_into_a_class(self):
        actual = self.parser.create_person()
        expected = Person(1, "ledge@sheg.com", "jonald", "cregg")
        self.assertEqual(actual.personal_id, expected.personal_id)
        self.assertEqual(actual.email, expected.email)
        self.assertEqual(actual.first_name, expected.first_name)
        self.assertEqual(actual.last_name, expected.last_name)

print("herpy derp")

cregg = Parser("1,ledge@sheg.com,jonald,cregg")
cregg_the_person = cregg.create_person()
cregg_the_person.say_hello()
cregg_the_person.print_email_provider()