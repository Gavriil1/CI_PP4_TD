from django.urls import path
from .views import contactform
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('contactform/', contactform, name='contactform'),
    ]