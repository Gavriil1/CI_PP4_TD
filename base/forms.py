from django import forms
from django.forms import ModelForm

from .models import Task


class DateInput(forms.DateInput):
    input_type = 'date'


class PostForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('user', 'title', 'description', 'completed', 'frequency', 'importance', 'due')
        
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),
            'frequency': forms.Select(attrs={'class': 'form-control'}),
            'importance': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'completed': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'due': forms.widgets.DateInput(attrs={'type': 'date'}),
        }


    # user
    # title 
    # description 
    # complete 
    # created
    # frequency
    # importance
    # completed
    # due