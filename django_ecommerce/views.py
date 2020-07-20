from django.shortcuts import render, redirect
from shop.models import Product
from django.contrib import messages
from contact.forms import SubscriberForm
from django.contrib.auth.models import User, auth
from django.http import HttpResponse

def home_page(request):
    products = Product.objects.all()[:8]
    forms = SubscriberForm()
    if request.method == 'POST':
        forms = SubscriberForm(request.POST)
        if forms.is_valid():
            forms.save()
    context = {
        'products': products,
        'forms': forms
    }
    return render(request, 'home.html', context)

