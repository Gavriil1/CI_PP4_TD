# from django.db import models
# from django.contrib.auth.models import User

# Create your models here.


# class Task(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
#     title = models.CharField(max_length=200)
#     description = models.TextField(null=True, blank=True)
#     complete = models.BooleanField(default=False)
#     created = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title

#     class Meta:
#         ordering = ['complete']
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Task(models.Model):
    FREQUENCY_CHOICES = [
        ('D', 'Daily Goal'),
        ('W', 'Weekly Goal'),
        ('M', 'Monthly Goal'),
        ('Y', 'Yearly Goal'),
    ]
    
    Important_Choice = [
        ('A', 'A Urgent'),
        ('B', 'B Important'),
        ('C', 'C OK'),
        ('D', 'D Delegate'),
        ('E', 'E Eliminate'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    frequency = models.CharField(max_length=10, choices=FREQUENCY_CHOICES, default='Daily')
    importance = models.CharField(max_length=10, choices=Important_Choice, default='A_Urgent')
    # due = models.DateField(default='2100-01-01')
    due = models.DateField(default=timezone.now().date())
    

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['complete']
