from django.contrib import admin
from .models import Task
# Register your models here.
# Contact
# admin.site.register(Task)
@admin.register(Task)

class AdminTaskView(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'importance', 'complete']
    list_filter = ['importance', 'frequency','user']
    search_fields = ['description']

