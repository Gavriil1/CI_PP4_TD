from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
