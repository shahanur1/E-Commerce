from django.shortcuts import render, redirect
from shop.models import Product
from django.contrib import messages
from contact.forms import SubscriberForm
from django.contrib.auth.models import User, auth
from django.http import HttpResponse

def logout(request):
    auth.logout(request)
    return redirect('home.html')
