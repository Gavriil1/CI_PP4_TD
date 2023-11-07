from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from books.models import Product
import json

class TestViews(TestCase):

    def setUp(self):
        """
        It creates a test user
        """
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_books_GET(self):
        """
        This test checks if the URL is generated correctly dynamically from the view name for login and register.
        It checks if the response for login and register URL is 200.
        It checks if the correct template was used to generate the login and register pages.
        """ 
        response = self.client.get(reverse('books'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'booksapp/books.html')
