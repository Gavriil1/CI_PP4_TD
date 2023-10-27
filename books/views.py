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
# importing pagination
from django.core.paginator import Paginator
from .models import Product


def books(request):
    products = Product.objects.all()
    #set up pagination.
    p = Paginator(Product.objects.all(), 2)
    page = request.GET.get('page')
    venues = p.get_page(page)
    # nums = "a" * venues.paginator.num_pages
    nums = range(1, venues.paginator.num_pages + 1)
    context = {
        'products': products,
        'venues': venues,
        'nums': nums,
        'current_page': int(page) if page else 1, 
    }
    return render(request, 'booksapp/books.html', context)


def test(request):
    products = Product.objects.all()
    #set up pagination.
    p = Paginator(Product.objects.all(), 2)
    page = request.GET.get('page')
    venues = p.get_page(page)
    # nums = "a" * venues.paginator.num_pages
    nums = range(1, venues.paginator.num_pages + 1)
    context = {
        'products': products,
        'venues': venues,
        'nums': nums,
        'current_page': int(page) if page else 1, 
    }
    return render(request, 'test.html', context)

