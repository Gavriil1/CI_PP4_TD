from django.test import SimpleTestCase
from django.urls import reverse, resolve
from books.views import books


class TestUrls(SimpleTestCase):

    def test_list_url_resolves(self):
        """
        It Checks if the homepage URL is resolved correctly.
        """
        url = reverse('books')
        print(resolve(url))
        self.assertEquals(resolve(url).func, books)
