from django import forms
from django.forms import ModelForm

from .models import Task


class DateInput(forms.DateInput):
    input_type = 'date'


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


