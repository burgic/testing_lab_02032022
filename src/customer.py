class Customer:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet

    def buy_drink(self, pub_name, drink_name):
        self.wallet -= drink_name.price
        pub_name.till += drink_name.price