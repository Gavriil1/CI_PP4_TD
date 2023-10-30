# Imports
# Third Party
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
# Internal:
from .models import Contact


@login_required
def contact_form(request):
    """
    This function allows user to send text or feedback to admin
    """
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.message = message
        contact.save()
        messages.success(
            request,
            "Message Received. We will get back to you soon! Thank you!")
        return redirect('tasks')
    return render(request, 'contactformapp/feedback.html')
