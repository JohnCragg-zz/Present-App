# from unittest import TestCase
# from mock import Mock
# from python.src.main.Item import Item
# from python.src.main.Person import Person
# from python.src.main.db import DB
#
# mark = Person('SparkyMark123@grinder.com', "Mark", "Holmes")
# john = Person("FredSaidIWasBoring@loser.com", "John", "Cragg")
# clarke = Person("NotClarkesFresher@warwick.ac.uk", "Clarke", "Clarkson")
# people_mark_cares_about = [mark, john, clarke]
#
# bike = Item("NotClarkesFresher@warwick.ac.uk", 'Coolbrand Bike', 150, 3, 'www.bikes.com')
# ps2 = Item("NotClarkesFresher@warwick.ac.uk", 'Playstation 2', 60, 4, 'www.game.com')
# bs = Item("NotClarkesFresher@warwick.ac.uk", 'Banana Suit', 55, 1, 'wwww.clerksfresh.org')
# banter = Item("FredSaidIWasABoring@loser.com", "Bants", 50000, 1, 'www.sportyjake.com')
# copas = Item("FredSaidIWasABoring@loser.com", "Copa Mundials", 90, 2, 'www.jjb.co.uk')
# clarkes_xmas_list = [bike, ps2, bs]
# creggs_xmas_list = [banter, copas]
#
#
# class TestDB(TestCase):
#     def setUp(self):
#         conn = Mock()
#         cursor = Mock()
#
#         self.db = DB(conn, cursor)
#
#     def test_can_parse_a_string_into_a_class(self):
#         self.db.populate_table(people_mark_cares_about, DB.insert_person)
#
#         self.db.populate_table(clarkes_xmas_list, DB.insert_item)
#         self.db.populate_table(creggs_xmas_list, DB.insert_item)
#
#
#         read_table(Person)
#         read_table(Item)
