from django.test import SimpleTestCase
from django.urls import reverse, resolve
from contactform.views import contact_form

class TestUrls(SimpleTestCase):

    def test_list_url_resolves(self):
        """
        It Checks if the homepage URL is resolved correctly.
        """
        url = reverse('feedback')  
        print(resolve(url))
        self.assertEquals(resolve(url).func, contact_form)


