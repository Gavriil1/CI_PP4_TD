# Imports
# Third party:
from django import forms
from django.forms import ModelForm
# Internal
from .models import Task


#  The class is used to give date type to DateInput
class DateInput(forms.DateInput):
    input_type = 'date'


# The class used to to create customized form for admin console
class PostForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'completed', 'frequency', 'importance', 'due')
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'frequency': forms.Select(attrs={'class': 'form-control'}),
            'importance': forms.Select(attrs={'class': 'form-control'}),     
            'completed': forms.Select(attrs={'class': 'form-control'}),
            'due': forms.widgets.DateInput(attrs={'type': 'date'}),
        }


