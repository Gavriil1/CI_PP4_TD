# Imports
# 3d party:
from django.urls import path
# Internal: 
from .views import books


# Url which show books on book page
urlpatterns = [
    path('books/', books, name='books'),
    ]