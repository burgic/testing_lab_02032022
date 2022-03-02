import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("derek", 10)

    def test_customer_has_name(self):
        self.assertEqual("derek", self.customer.name)
    
    def test_customer_has_wallet(self):
        self.assertEqual(10, self.customer.wallet)

    