import unittest
from src.drinks import Drinks

class TestDrinks(unittest.TestCase):
    def setUp(self):
        self.drinks = Drinks("Guinness", 5.00)

    def drink_has_name(self):
        self.assertEqual("Guinness", self.drinks.name)

    def drink_has_price(self):
        self.assertEqual(5.00, self.drinks.price)

    