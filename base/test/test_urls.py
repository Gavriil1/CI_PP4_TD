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


    


