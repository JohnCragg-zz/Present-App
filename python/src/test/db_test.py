import sqlite3
from unittest import TestCase

from python.src.main.Item import Item
from python.src.main.Person import Person
from python.src.main.db import DB

clarke = Person("NotClarkesFresher@warwick.ac.uk", "Clarke", "Clarkson")
marks_friends = [clarke]

bike = Item("NotClarkesFresher@warwick.ac.uk", "Coolbrand Bike", 150, 3, "www.bikes.com")
ps2 = Item("NotClarkesFresher@warwick.ac.uk", "Playstation 2", 60, 4, "www.game.com")

items = [bike, ps2]


class TestDB(TestCase):
    def setUp(self):
        conn = sqlite3.connect("test.db")
        cursor = conn.cursor()
        self.db = DB(cursor, conn)
        self.db.cursor.execute("DROP TABLE IF EXISTS Person")
        self.db.cursor.execute("DROP TABLE IF EXISTS Item")
        self.db.create_person_table()
        self.db.create_item_table()

    def test_can_parse_a_string_into_a_class(self):
        self.db.populate_table(marks_friends, self.db.insert_person)
        self.db.populate_table(items, self.db.insert_item)
        created_items = self.db.create_item_from_table("NotClarkesFresher@warwick.ac.uk")
        self.assertEqual(len(created_items), len(items))
        for i in range(len(created_items)):
            self.are_items_equal(created_items[i], items[i])

    def are_items_equal(self, actual, expected):
        self.assertEqual(actual.person_email, expected.person_email)
        self.assertEqual(actual.name, expected.name)
        self.assertEqual(actual.price, expected.price)
        self.assertEqual(actual.priority, expected.priority)
        self.assertEqual(actual.hyperlink, expected.hyperlink)
