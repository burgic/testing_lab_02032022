class Customer:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkeness_level = 0

    def check_age(self):
        return self.age >= 18
    
    def check_drunkenness(self):
        return self.drunkeness_level < 24

    def buy_drink(self, pub_name, drink_name):
        if self.check_age():
            if self.check_drunkenness():
                self.wallet -= drink_name.price
                pub_name.till += drink_name.price
                self.drunkeness_level += drink_name.alcohol_level
            else:
                return "not tonight"
        else:
            return "nae bairns"
        
    def buy_food(self, pub_name, food_name):
        self.wallet -= food_name.price
        pub_name.till += food_name.price
        self.drunkeness_level -= food_name.rejuvenation_level
        