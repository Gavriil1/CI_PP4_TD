from django.test import TestCase, Client
from django.urls import reverse
from base.models import Task
import json

class TestViews(TestCase):

    def test_project_list_GET(self):
        client = Client()
        response = client.get(reverse('tasks'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateNotUsed(response, 'base/homepage.html')