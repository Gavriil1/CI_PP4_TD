from django.urls import path
from .views import books
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('books/', books, name='books'),
    ]