from django.urls import path
from .views import TaskDetail, TaskCreate, TaskUpdate, DeleteView, CustomLoginView, RegisterPage,   manual, homepage, custom_404, test, custom_404,  books
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', homepage, name='tasks'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('manual/', manual, name='manual'), 
    path('register/', RegisterPage.as_view(), name='register'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', DeleteView.as_view(), name='task-delete'),
    path('test/', test, name='test'),
    path('custom_404/', custom_404, name='custom_404'),
    # path('feedback/', feedback, name='feedback'), 
    path('books/', books, name='books'), 
    ]