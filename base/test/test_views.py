from django.test import TestCase, Client
from django.urls import reverse
from base.models import Task
import json

from django.contrib.auth.models import User  # Add this import

class NonAuthViews(TestCase):
    # ok
    # testing login view
    def test_project_list_GET_login(self):
        client = Client()
        response = client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/login.html')
    #ok
    # register page
    def test_project_list_GET_register(self):
        client = Client()
        response = client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/register.html')



class AuthViews(TestCase):

    def setUp(self):
        # Create a test user and log them in
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        # Creating a task for  temporary database
        self.task = Task.objects.create(title='Test Task', description='This is a test task', user=self.user)
    # ok
    def test_project_list_GET(self):
        response = self.client.get(reverse('tasks'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/homepage.html')
    # ok
    # checking if create task works
    def test_project_list_GET_create_task(self):
        response = self.client.get(reverse('task-create'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/task_form.html')
    #ok
    def test_project_list_GET_manual(self):
        response = self.client.get(reverse('manual'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/manual.html')

    #  here I check if crated task in the database is ok.
    # ok
    def test_project_list_GET_task(self):
        # Replace '1' with a valid Task primary key
        task_pk = 1  # Change this to a valid primary key
        response = self.client.get(reverse('task', kwargs={'pk': task_pk}))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/task.html')

    # checking if update view works well
    #ok 
    def test_project_list_GET_task(self):
        # Replace '1' with a valid Task primary key
        task_pk = 1  # Change this to a valid primary key
        response = self.client.get(reverse('task-update', kwargs={'pk': task_pk}))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/task_form.html')

    # ok
    # checking if deleteview rorks well.
    def test_project_list_GET_task_delete(self):
        # Replace '1' with a valid Task primary key
        task_pk = 1  # Change this to a valid primary key
        response = self.client.get(reverse('task-delete', kwargs={'pk': task_pk}))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/task_confirm_delete.html')
    # ok
    # logout view checking if it redirects.
    def test_project_list_GET_logoutview(self):
        response = self.client.get(reverse('logout'))
        self.assertEquals(response.status_code, 302)
        



