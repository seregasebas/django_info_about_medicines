from django.test import TestCase
from mixer.backend.django import mixer
from .models import Contacts
# from user_app.models import MedUser


# Create your tests here.

class ContactsTestCase(TestCase):

    def setUp(self):
        self.name = 'serega'
        self.email = 'test@test.com'
        self.message = 'Hello, word!'

    def test_is_message(self):
        self.assertFalse(Contacts.is_name(self))
        self.assertFalse(Contacts.is_email(self))
        self.assertFalse(Contacts.is_message(self))

    def test_is_hello_contacts(self):
        self.assertTrue(Contacts.hello_contacts(self)=='Hello, programmer!')

    def test_str(self):
        self.assertEqual(str(self.message), 'Hello, word!')

# Тест через Mixer
class ContactsTestMixer(TestCase):

    def setUp(self):
        self.contacts = mixer.blend(Contacts)

    def test_is_message(self):
        self.assertFalse(Contacts.is_name(self.contacts))
        self.assertFalse(Contacts.is_email(self.contacts))
        self.assertFalse(Contacts.is_message(self.contacts))