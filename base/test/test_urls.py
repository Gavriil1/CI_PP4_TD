from django.test import SimpleTestCase
from django.urls import reverse, resolve
from base.views import CustomLoginView, RegisterPage, TaskDetail, TaskCreate, TaskUpdate, DeleteView, TaskList, homepage, manual


class TestUrls(SimpleTestCase):

    def test_list_url_is_resolved_homepage(self):
        url = reverse('tasks')
        print(resolve(url))
        self.assertEquals(resolve(url).func, homepage)

    def test_list_url_is_resolved_manual(self):
        url = reverse('manual')
        print(resolve(url))
        self.assertEquals(resolve(url).func, manual)

    def test_list_url_is_resolved_login(self):
        url = reverse('login')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, CustomLoginView)

    def test_list_url_is_resolved_register(self):
        url = reverse('register')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, RegisterPage)

    def test_list_url_is_resolved_taskdetail(self):
        task_id = 1  # for the test to work I need to use the valid id
        url = reverse('task', kwargs={'pk': task_id})
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, TaskDetail)

    def test_list_url_is_resolved_task_create(self):
        url = reverse('task-create')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, TaskCreate)

    def test_list_url_is_resolved_task_update(self):
        task_id = 1  # for the test to work I need to use the valid id
        url = reverse('task-update', kwargs={'pk': task_id})
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, TaskUpdate)

    def test_list_url_is_resolved_task_delete(self):
        task_id = 1  # for the test to work I need to use the valid id
        url = reverse('task-delete', kwargs={'pk': task_id})
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, DeleteView)


    


