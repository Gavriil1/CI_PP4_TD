from django.test import TestCase, Client
from django.urls import reverse
from base.models import Task
from django.contrib.auth.models import User
import json


"""
This test checks if the URL is generated correctly dynamically from the view
name for login and register. It checks if the response for login and register
URL is 200. It checks if the correct template was used to generate the
login and register pages.
"""


class NonAuthViews(TestCase):
    def test_project_list_GET_login(self):
        client = Client()
        response = client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login-register/login.html')

    def test_project_list_GET_register(self):
        client = Client()
        response = client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login-register/register.html')


"""
This test checks if the URL is generated correctly dynamically from the
view name for Homepage, Manual, Create Page, Update Page, Delete Page.
It checks if the  URL response for the tested pages is 200.It checks i
the correct template was used to generate tested pages.
"""


class AuthViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='test', password='test')
        self.client.login(username='test', password='test')
        self.task = Task.objects.create(
            title='Test Task', description='This is a test', user=self.user)

    def test_project_list_GET(self):
        response = self.client.get(reverse('tasks'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'todoapp-create-update-delete/homepag.html')

    def test_project_list_GET_create_task(self):
        response = self.client.get(reverse('task-create'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'todoapp-create-update-delete/task_form.html')

    def test_project_list_GET_manual(self):
        response = self.client.get(reverse('manual'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'todoapp-create-update-delete/manual.html')

    def test_project_list_GET_task(self):
        task_pk = 1
        response = self.client.get(reverse('task', kwargs={'pk': task_pk}))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/task.html')

    def test_project_list_GET_task(self):
        task_pk = 1
        response = self.client.get(
            reverse('task-update', kwargs={'pk': task_pk}))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(
         response, 'todoapp-create-update-delete/task_form.html')

    def test_project_list_GET_task_delete(self):
        task_pk = 1
        response = self.client.get(reverse(
            'task-delete', kwargs={'pk': task_pk}))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'todoapp-create-update-delete/task_confirm_delete.html')

    def test_project_list_GET_logoutview(self):
        response = self.client.get(reverse('logout'))
        self.assertEquals(response.status_code, 302)
