from django.urls import path
from .views import books, test
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('books/', books, name='books'),
    path('test/', test, name='test'),
    ]