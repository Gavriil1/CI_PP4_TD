from django.urls import path
from .views import contact_form
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('feedback/', contact_form, name='feedback'),
    ]