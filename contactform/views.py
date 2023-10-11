from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.urls import path
from . import views
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.
def contactform(request):
    if request.method == "POST":
        contact = Contact()  # Create a new instance of the Contact model
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')  # Get the subject field
        message = request.POST.get('message')  # Get the message field
        
        # Set the values for the Contact instance
        contact.name = name
        contact.email = email
        contact.subject = subject  # Assign the subject value
        contact.message = message  # Assign the message value
        
        contact.save()  # Save the Contact instance to the database
        
        # return HttpResponse("<h1>THANKS FOR CONTACTING US<h1>")
        return render(request, "/workspace/CI_PP4_TD/templates/feedbackreceived.html")
    return render(request, '/workspace/CI_PP4_TD/templates/feedback.html')