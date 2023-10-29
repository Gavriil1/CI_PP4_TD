# Imports
# External:
from django.apps import AppConfig
# Internal:


class BaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base'
