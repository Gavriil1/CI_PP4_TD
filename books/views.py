# Imports
#3d party:
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
# internal: 
from .models import Product


@login_required
def books(request):
    """
    This page load books and creates pagination
    """
    products = Product.objects.all()
    p = Paginator(Product.objects.all(), 2)
    page = request.GET.get('page')
    venues = p.get_page(page)
    nums = range(1, venues.paginator.num_pages + 1)
    context = {
        'products': products,
        'venues': venues,
        'nums': nums,
        'current_page': int(page) if page else 1, 
    }
    return render(request, 'booksapp/books.html', context)



