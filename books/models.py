
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Product(models.Model):
    title = models.CharField(max_length=200)
    details = models.TextField()
    stars = models.IntegerField(null=True)
    numberreviews = models.IntegerField(null=True)
    price = models.IntegerField(null=True)
    productpic = models.URLField(max_length=200)
    amazon = models.URLField(max_length=200)

    def __str__(self):
        return self.title