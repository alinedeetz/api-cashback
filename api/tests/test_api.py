from django.urls import reverse
from rest_framework.reverse import reverse as api_reverse
from rest_framework.test import APITestCase
from api.models import *

from django.contrib.auth import get_user_model

User = get_user_model()

class UserAPITestCase(APITestCase):
    def setUp(self):
        user = User.objects.create(username='test', email='hello@test.com', first_name='Test', last_name='User')
        user.set_password('passwordhere')
        user.save()

        client = Client.objects.create(first_name='Test', last_name='Client', document='12312312323', address='Rua lalala, 123',email='testclient@test.com')
        self.client.force_authenticate(user=user)

        product = Product.objects.create(product='product', price=10)

    def test_created_user_standard(self):
        queryset = User.objects.filter(username='test')
        self.assertEqual(queryset.count(),1)
    
    def test_create_client(self):
        response = self.client.post('/clients/', {
            'first_name': 'Test',
            'last_name': 'Client',
            'document': '12312312323',
            'address': 'Rua lalala, 123',
            'email': 'testclient@test.com'
        }).json()

        # print(response)
        self.assertEqual(response['first_name'], 'Test')

    def test_create_order(self):
        response = self.client.post('/orders/', {'client': 1, 'product': 1, 'qty': 1})
        print(response.json())
    
    def test_list_orders(self):
        response = self.client.get('/orders/')
        print(response.json())