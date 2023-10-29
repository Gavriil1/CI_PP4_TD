# Imports
# Third Party:
from django.contrib import admin
from django.contrib.auth.models import Group

# Internal:
from .models import Task

# Unregister groups from admin snce I do not use them
admin.site.unregister(Group)


# Register Task view to the admin conso9le
@admin.register(Task)
# with the bollow class I add more options to Task form in admin view
class AdminTaskView(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'importance', 'complete']
    list_filter = ['importance', 'frequency', 'user']
    search_fields = ['description']
