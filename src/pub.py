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
        if customer.age >= 18 and customer.drunkenness < 25.8:
            self.till += drink.price
            customer.wallet -= drink.price
            customer.drunkenness += drink.alcohol_level

    def sell_food(self, food, customer):
        customer.drunkenness -= food.rejuvenation_level
        customer.wallet -= food.price
        

   
