from django.shortcuts import render

import os

# Create your views here.


def index(request):
    # settings.py

    context = {'hello': 'Hello World'
    }
    return render(request, 'my_app/index.html', context)


def my_custom_error_view(request,exception):
     return render(request,'my_app/500.html')

def page_not_found_view(request,exception):
     return render(request,'my_app/404.html')

def my_custom_permission_denied_view(request,exception):
     return render(request,'my_app/403.html')

def my_custom_bad_request_view(request,exception):
     return render(request,'my_app/400.html')          

handler500 = 'my_app.views.my_custom_error_view'
handler404 = 'my_app.views.page_not_found_view'
handler403 = 'my_app.views.my_custom_permission_denied_view'
handler400 = 'my_app.views.my_custom_bad_request_view'