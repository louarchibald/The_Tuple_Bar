import unittest
from src.pub import Pub
from src.customer import Customer
from src.drinks import Drinks
from src.food import Food

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The Tuple Bar", 100.00)
        self.customer = Customer("Lou", 32, 50.00)
        self.drink = Drinks("Guinness", 5.00, 4.3)
        self.food = Food("Burger", 8.00, 4.3)
        


    def test_pub_has_name(self):
        self.assertEqual("The Tuple Bar", self.pub.name)

    def test_drink_in_stock(self):
        self.pub.add_stock("Guinness")
        self.assertEqual(1, len(self.pub.drinks))

    def test_customer_can_buy_drink(self):
        self.pub.sell_drink(self.drink, self.customer)
        self.assertEqual(45.00, self.customer.wallet)
        self.assertEqual(105.00, self.pub.till)

    def test_sell_food(self):
        self.pub.sell_food(self.food, self.customer)
        self.assertEqual(-4.3, self.customer.drunkenness)
    

