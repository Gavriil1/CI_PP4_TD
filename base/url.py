# Imports
# External:
from django.urls import path
from django.contrib.auth.views import LogoutView
# Internal:
from .views import TaskCreate, TaskUpdate, DeleteView, CustomLoginView
from .views import RegisterPage,   manual, homepage, custom_404


# Crete urls which allows us to have Login, Register, Logout Tasklist, Update Tasks, Create Tasks, Delete Tasks.
urlpatterns = [
    path('', homepage, name='tasks'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('manual/', manual, name='manual'), 
    path('register/', RegisterPage.as_view(), name='register'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', DeleteView.as_view(), name='task-delete'),
    path('custom_404/', custom_404, name='custom_404'),
    ]