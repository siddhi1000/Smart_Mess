from django.test import TestCase
from apps.menus.models import Menu

class MenuModelTest(TestCase):
    def setUp(self):
        Menu.objects.create(name="Breakfast Menu", description="A variety of breakfast options", price=5.00)
        Menu.objects.create(name="Lunch Menu", description="A selection of lunch meals", price=7.50)

    def test_menu_creation(self):
        breakfast_menu = Menu.objects.get(name="Breakfast Menu")
        lunch_menu = Menu.objects.get(name="Lunch Menu")
        self.assertEqual(breakfast_menu.description, "A variety of breakfast options")
        self.assertEqual(lunch_menu.price, 7.50)

    def test_menu_str(self):
        menu = Menu.objects.get(name="Breakfast Menu")
        self.assertEqual(str(menu), "Breakfast Menu")