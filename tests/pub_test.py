import unittest
from src.drink import Drink
from src.pub import Pub

class TestPub (unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)
    
    def test_increase_till(self):
        self.pub.increase_till(2.50)
        expected = 102.5
        actual = self.pub.till
        self.assertEqual(expected, actual)
        # self.assertEqual(102.5, self.pub.till)

    def test_pub_has_till(self):
        self.assertEqual(100.00, self.pub.till)
    
    def test_pub_has_drinks(self):
        tennants = Drink("Tennants", 1.50)
        self.pub.add_drink(tennants)
        range = self.pub.return_range_drinks()
        self.assertEqual(1, range)