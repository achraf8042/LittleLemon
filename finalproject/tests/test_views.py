from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):

    def setUp(self):
        # Add a few test instances of the Menu model
        self.menu1 = Menu.objects.create(title="Pizza", price=10.00, inventory=5)
        self.menu2 = Menu.objects.create(title="Burger", price=8.50, inventory=8)
        self.menu3 = Menu.objects.create(title="Pasta", price=12.00, inventory=12)

    def test_getall(self):
        # Retrieve all the Menu objects added for the test purpose
        menus = Menu.objects.all()
        
        # Serialize the data
        serialized_data = MenuSerializer(menus, many=True).data
        expected_data = [
            {'id': self.menu1.id, 'title': 'Pizza', 'price': 10.00, 'inventory': 5},
            {'id': self.menu2.id, 'title': 'Burger', 'price': 8.50, 'inventory':8},
            {'id': self.menu3.id, 'title': 'Pasta', 'price': 12.00, 'inventory': 12}
        ]
        
        # Assert that the serialized data equals the expected data[
        self.assertEqual(serialized_data, expected_data)
