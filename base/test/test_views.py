from django.test import TestCase, Client
from django.urls import reverse
from base.models import Task
import json

from django.contrib.auth.models import User  # Add this import

class TestViews(TestCase):

    def setUp(self):
        # Create a test user and log them in
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        # Creating a task for  temporary database
        self.task = Task.objects.create(title='Test Task', description='This is a test task', user=self.user)

    def test_project_list_GET(self):
        response = self.client.get(reverse('tasks'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/homepage.html')

    def test_project_list_GET_manual(self):
        response = self.client.get(reverse('manual'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/manual.html')

    def test_project_list_GET_manual(self):
        response = self.client.get(reverse('manual'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/manual.html')

    #  here I check if crated task in the database is ok.

    def test_project_list_GET_task(self):
        # Replace '1' with a valid Task primary key
        task_pk = 1  # Change this to a valid primary key
        response = self.client.get(reverse('task', kwargs={'pk': task_pk}))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/task.html')

