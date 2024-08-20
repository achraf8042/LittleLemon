from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):

    def setUp(self):
        # Add a few test instances of the Menu model
        self.menu1 = Menu.objects.create(name="Pizza", price=10.00)
        self.menu2 = Menu.objects.create(name="Burger", price=8.50)
        self.menu3 = Menu.objects.create(name="Pasta", price=12.00)

    def test_getall(self):
        # Retrieve all the Menu objects added for the test purpose
        menus = Menu.objects.all()
        
        # Serialize the data
        serialized_data = MenuSerializer(menus, many=True).data
        
        # Expected data
        expected_data = [
            {'id': self.menu1.id, 'name': 'Pizza', 'price': '10.00'},
            {'id': self.menu2.id, 'name': 'Burger', 'price': '8.50'},
            {'id': self.menu3.id, 'name': 'Pasta', 'price': '12.00'}
        ]
        
        # Assert that the serialized data equals the expected data
        self.assertEqual(serialized_data, expected_data)
