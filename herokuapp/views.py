from django.shortcuts import render

import os

# Create your views here.


def index(request):
    # settings.py

    context = {'hello': 'Hello World'
    }
    return render(request, 'herokuapp/index.html', context)