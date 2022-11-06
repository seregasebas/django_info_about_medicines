from django.test import Client
from django.test import TestCase
from faker import Faker
from user_app.models import MedUser

class OpenViewsTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.fake = Faker()

    def test_statuses(self):
        #get 
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/comments_view/')
        self.assertEqual(response.status_code, 200)

        response = self.client.post('/comments_create/')
        self.assertEqual(response.status_code, 302)
         
        #post
        MedUser.objects.create_user(username='testuser', email='test11@ys.com', password='seo1234567')
        self.client.login(username='testuser', password='seo1234567')
        response = self.client.post('/comments_create/', {'name':self.fake.name(), 
                                    'email':self.fake.email(), 'message':self.fake.text()})
        self.assertEqual(response.status_code, 302)

    def test_login_required(self):
        MedUser.objects.create_user(username='testuser', email='test11@ys.com', password='seo1234567')
        #клиент не вошел
        response = self.client.get('/comments_create/')
        self.assertEqual(response.status_code, 302)
        #логиним его
        self.client.login(username='testuser', password='seo1234567')

        response = self.client.get('/comments_create/')
        self.assertEqual(response.status_code, 200)