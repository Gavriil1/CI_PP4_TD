from django.contrib import admin
from .models import Task
# Register your models here.

# admin.site.register(Task)
@admin.register(Task)

class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'importance']
