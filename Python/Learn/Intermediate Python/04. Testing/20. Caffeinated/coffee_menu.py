class CoffeeMenu:

    def __init__(self):
        self.menu = {
            'espresso': 2.00, 
            'double espresso': 3.00,
            'americano': 2.50,
            'latte': 3.50,
            'flat white': 3.50,
            'cappucino': 3.70,
            'mocha': 4.00
        }

    def get_price(self, item):
        return self.menu.get(item.lower())
    
    def add_item(self, item, price):
        self.menu[item.lower()] = price