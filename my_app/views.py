from django.shortcuts import render, redirect
import os
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

from .models import Contact, ContactForm

# Create your views here.

def index(request):
    # settings.py

     contacts = Contact.objects.all()

     if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
     else:
        form = ContactForm()
     print(contacts)
     context = {
          'contacts': contacts,
          'form': form,
          'test': 'test'
          }

     return render(request, 'index.html', context)

#     
#     return render(request, 'index.html', context)



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def my_custom_error_view(request):
     return render(request,'errors/500.html')

def page_not_found_view(request,exception):
     return render(request,'errors/404.html')

def my_custom_permission_denied_view(request,exception):
     return render(request,'errors/403.html')

def my_custom_bad_request_view(request,exception):
     return render(request,'errors/400.html')          

