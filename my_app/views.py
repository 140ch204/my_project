from django.shortcuts import render, redirect
import os
from django.contrib.auth import authenticate, login, logout

# Create your views here.



def index(request):
    # settings.py

    context = {'hello': 'Hello World'
    }
    return render(request, 'index.html', context)

def my_custom_error_view(request):
     return render(request,'errors/500.html')

def page_not_found_view(request,exception):
     return render(request,'errors/404.html')

def my_custom_permission_denied_view(request,exception):
     return render(request,'errors/403.html')

def my_custom_bad_request_view(request,exception):
     return render(request,'errors/400.html')          

