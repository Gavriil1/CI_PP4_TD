from django import forms
from .models import Task


class PostForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('user', 'title', 'description', 'complete')
        
        widgets = {
            'user': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'complete': forms.Select(attrs={'class': 'form-control'}),
        }
