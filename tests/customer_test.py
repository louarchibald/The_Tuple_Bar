import unittest
from src.customer import Customer
from src.drinks import Drinks
from src.pub import Pub

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Lou", 32, 50.00)
        self.customer2 = Customer("Jonny", 33, 10.00)
        self.drinks = Drinks("Guinness", 5.00, 4.3)
        self.pub = Pub("The Tuple Bar", 100.00)

    def test_customer_has_name(self):
        self.assertEqual("Lou", self.customer.name)

    def test_customer_has_money(self):
        self.assertEqual(50.00, self.customer.wallet)

    def test_customer_gets_drunk(self):
        self.pub.sell_drink(self.drinks, self.customer)
        self.assertEqual(4.3, self.customer.drunkenness)

    def test_customer2_gets_drunk(self):
        self.pub.sell_drink(self.drinks, self.customer2)
        self.pub.sell_drink(self.drinks, self.customer2)
        self.pub.sell_drink(self.drinks, self.customer2)
        self.pub.sell_drink(self.drinks, self.customer2)
        self.pub.sell_drink(self.drinks, self.customer2)
        self.pub.sell_drink(self.drinks, self.customer2)
        self.assertEqual(25.8, self.customer2.drunkenness)



