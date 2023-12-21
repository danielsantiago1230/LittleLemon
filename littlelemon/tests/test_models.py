from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_menu_creation(self):
        menu = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(menu.title, "IceCream")
        self.assertEqual(menu.price, 80)
