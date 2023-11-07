from django.test import SimpleTestCase
from django.urls import reverse, resolve
from base.views import CustomLoginView, RegisterPage,  TaskCreate, TaskUpdate, DeleteView,  homepage, manual


class TestUrls(SimpleTestCase):

    def test_list_url_is_resolved_homepage(self):
        """
        Checks if the homepage URL is resolved correctly.
        """
        url = reverse('tasks')
        print(resolve(url))
        self.assertEquals(resolve(url).func, homepage)

    def test_list_url_is_resolved_manual(self):
        """
        Checks if the manual URL is resolved correctly.
        """
        url = reverse('manual')
        print(resolve(url))
        self.assertEquals(resolve(url).func, manual)

    def test_list_url_is_resolved_login(self):
        """
        Checks if the login URL is resolved correctly.
        """
        url = reverse('login')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, CustomLoginView)

    def test_list_url_is_resolved_register(self):
        """
        Checks if the register URL is resolved correctly.
        """
        url = reverse('register')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, RegisterPage)


    def test_list_url_is_resolved_task_create(self):
        """
        Checks if the create-task URL is resolved correctly.
        """
        url = reverse('task-create')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, TaskCreate)

    def test_list_url_is_resolved_task_update(self):
        """
        Checks if the update page URL is resolved correctly.
        """
        task_id = 1  
        url = reverse('task-update', kwargs={'pk': task_id})
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, TaskUpdate)

    def test_list_url_is_resolved_task_delete(self):
        task_id = 1  
        url = reverse('task-delete', kwargs={'pk': task_id})
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, DeleteView)


    


