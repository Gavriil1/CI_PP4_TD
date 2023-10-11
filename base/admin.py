from django.contrib import admin
from .models import Task,  Product
# Register your models here.
# Contact
# admin.site.register(Task)
@admin.register(Task)

class AdminTaskView(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'importance', 'complete']
    list_filter = ['importance', 'frequency','user']
    search_fields = ['description']


# admin.site.register(Contact)


admin.site.register(Product)




#   user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
#     title = models.CharField(max_length=200)
#     description = models.TextField(null=True, blank=True)
#     complete = models.BooleanField(default=False)
#     created = models.DateTimeField(auto_now_add=True)
#     frequency = models.CharField(max_length=10, choices=FREQUENCY_CHOICES, default='Daily')
#     importance = models.CharField(max_length=10, choices=Important_Choice, default='Urgent')
#     completed = models.CharField(max_length=10, choices=COMPLETED_CHOICE, default='InComplete')