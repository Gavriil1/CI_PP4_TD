# Imports
# Third party:
from django.urls import path
# Internal:
from .views import contact_form

# This create link to contact form, which user may use to send a feedback to admin

urlpatterns = [
    path('feedback/', contact_form, name='feedback'),
    ]