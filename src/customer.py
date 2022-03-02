class Customer:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age

    def check_age(self):
        return self.age >= 18

    def buy_drink(self, pub_name, drink_name):
        self.wallet -= drink_name.price
        pub_name.till += drink_name.price