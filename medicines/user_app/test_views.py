from django.test import Client
from django.test import TestCase
from faker import Faker

class OpenViewsTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.fake = Faker()

    #get 
    def test_statuses(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/comments_view/')
        self.assertEqual(response.status_code, 200)
    