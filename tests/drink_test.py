import unittest
from src.drink import Drink

class TestDrink (unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Tennants", 1.50)

    def test_drink_has_name(self):
        self.assertEqual("Tennants", self.drink.name)
    
    def test_drink_has_price(self):
        self.assertEqual(1.50, self.drink.price)
    