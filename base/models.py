# Imports
# External:
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Internal:


class Task(models.Model):
    FREQUENCY_CHOICES = [
        ('Daily', 'Daily'),
        ('Weekly', 'Weekly'),
        ('Monthly', 'Monthly'),
        ('Yearly', 'Yearly'),
    ]
    
    Important_Choice = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
    ]

    COMPLETED_CHOICE = [
        ('Completed', 'Completed'),
        ('InComplete', 'InComplete'),

    ]    

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    frequency = models.CharField(max_length=10, choices=FREQUENCY_CHOICES, default='Daily')
    importance = models.CharField(max_length=10, choices=Important_Choice, default='A')
    completed = models.CharField(max_length=10, choices=COMPLETED_CHOICE, default='InComplete')
    due = models.DateField(default=timezone.now().date())
    

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['complete']
