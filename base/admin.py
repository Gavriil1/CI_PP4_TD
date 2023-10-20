from django.contrib import admin
from .models import Task
from django.contrib.auth.models import Group
# Register your models here.
# Contact
# admin.site.register(Task)

# unregister groups: https://www.youtube.com/watch?v=6YxyKBl0M-g
admin.site.unregister(Group)

@admin.register(Task)

class AdminTaskView(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'importance', 'complete']
    list_filter = ['importance', 'frequency','user']
    search_fields = ['description']

