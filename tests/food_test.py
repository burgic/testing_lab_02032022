import unittest
from src.food import Food

class TestFood(unittest.TestCase):
    def setUp(self):
        self.food = Food("chips", 4.50, 2)
    
    def test_food_has_name(self):
        self.assertEqual("chips", self.food.name)
    
    def test_food_has_price(self):
        self.assertEqual(4.5, self.food.price)
    
    def test_food_has_rejuvenation_level(self):
        self.assertEqual(2, self.food.rejuvenation_level)
