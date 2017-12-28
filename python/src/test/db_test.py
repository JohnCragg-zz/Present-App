import sqlite3
from unittest import TestCase

from python.src.main.Item import Item
from python.src.main.Person import Person
from python.src.main.db import DB

clarke = Person("NotClarkesFresher@warwick.ac.uk", "Clarke", "Clarkson")
marks_friends = [clarke]
bike = Item("NotClarkesFresher@warwick.ac.uk", "Coolbrand Bike", 150, 3, "www.bikes.com")
items = [bike]


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
        expected = ["NotClarkesFresher@warwick.ac.uk", "Coolbrand Bike", 150, 3, "www.bikes.com"]
        created_items = self.db.get_items("NotClarkesFresher@warwick.ac.uk")
        self.assertEqual(created_items, expected)
