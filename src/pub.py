class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []

    def increase_till(self, amount):
        self.till += amount
    
    def add_drink(self, drink):
        self.drinks.append(drink)
    
    def return_range_drinks(self):
        return len(self.drinks)