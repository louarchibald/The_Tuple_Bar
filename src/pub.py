class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []

    def increase_till(self, amount):
        self.till += amount

    def add_stock(self, drink):
        self.drinks.append(drink)

    def sell_drink(self, drink, customer):
        self.till += drink.price
        customer.wallet -= drink.price
