from django.shortcuts import render, redirect
from shop.models import Product
from django.contrib import messages
from contact.forms import SubscriberForm
from django.contrib.auth.models import User, auth
from django.http import HttpResponse

def login(request):
    
    if request.method == 'POST':
        print(request.method)
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/home')
        else:
            print('invalid credentials')
            messages.info(request, 'invalid credentials')
            return redirect('login.html')

    else:
        print('Go to login page')
        return render(request, 'login.html')


