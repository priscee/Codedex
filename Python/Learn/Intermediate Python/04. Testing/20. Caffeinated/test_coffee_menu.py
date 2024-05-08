import unittest
from coffee_menu import CoffeeMenu

class TestCoffeeMenu(unittest.TestCase):

    def setUp(self):
        self.menu = CoffeeMenu()
    
    def test_get_price_existing_item(self):
        self.assertEqual(self.menu.get_price('americano'), 2.50)
    
    def test_get_price_non_existing_item(self):
        self.assertIsNone(self.menu.get_price('kopi'))
        #kopi means coffee in Malay, a term used with other lingos in the Singapore coffee culture, especially in the coffee shops aka kopitiam

    def test_add_item(self):
        self.menu.add_item('piccolo', 3.20)
        self.assertEqual(self.menu.get_price('piccolo'), 3.20)

if __name__ == '__main__':
    unittest.main()