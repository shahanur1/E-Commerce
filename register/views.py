from django.shortcuts import render, redirect
from shop.models import Product
from django.contrib import messages
from contact.forms import SubscriberForm
from django.contrib.auth.models import User, auth
from django.http import HttpResponse

def registration(request):

    if request.method == 'POST':

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email_address = request.POSt['email_address']
        username = request.POST['username']
        password = request.POST['password']

        if password == password:
            
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exist!')
                return redirect('register')

            elif User.objects.filter(email_address=email_address).exists():
                messages.info(request, 'Email already exist!')
                return redirect('register')

            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email_address=email_address, password=password)
                user.save()
                return redirect('login.html')
            
        else:
            print('Password not matching.....')
            messages.info(request, 'Password not matching...')
            return redirect('register')

    else:
        return render(request, 'registration.html')

