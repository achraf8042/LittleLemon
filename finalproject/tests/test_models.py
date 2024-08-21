# tests/test-models.py

from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_menu_str_method(self):
        # Create an instance of the Menu model
        menu = Menu.objects.create(
            title='Cheeseburger',
            price=9.99,
            inventory=50
        )
        
        # Define the expected string representation
        expected_str = 'Cheeseburger'
        
        # Compare the actual string representation with the expected value
        self.assertEqual(str(menu), expected_str)
