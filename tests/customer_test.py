import unittest
from src.customer import Customer
from src.drink import Drink
from src.pub import Pub

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("derek", 10, 18)

    def test_customer_has_name(self):
        self.assertEqual("derek", self.customer.name)
    
    def test_customer_has_wallet(self):
        self.assertEqual(10, self.customer.wallet)

    def test_can_customer_check_age_true(self):
        status = self.customer.check_age()
        self.assertEqual(True, status)
        
    def test_can_customer_check_age_false(self):
        self.customer.age = 17
        status = self.customer.check_age()
        self.assertEqual(False, status)

    def test_customer_buy_drink(self):
        drink_lager = Drink("Tennants", 1.50, 2.4)
        pub_name = Pub("The Prancing Pony", 100)
        self.customer.buy_drink(pub_name, drink_lager)
        self.assertEqual(8.50, self.customer.wallet)
        self.assertEqual(101.5, pub_name.till)

    def test_underage_customer_buy_drink(self):
        self.customer.age = 17
        drink_lager = Drink("Tennants", 1.50, 2.4)
        pub_name = Pub("The Prancing Pony", 100)
        self.customer.buy_drink(pub_name, drink_lager)
        self.assertEqual(10, self.customer.wallet)
        self.assertEqual(100, pub_name.till)