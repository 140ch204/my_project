"""my_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf.urls import include, url
from my_app import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^$', views.index),
    path('overtherainbow/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]

handler500 = 'my_app.views.my_custom_error_view'
handler404 = 'my_app.views.page_not_found_view'
handler403 = 'my_app.views.my_custom_permission_denied_view'
handler400 = 'my_app.views.my_custom_bad_request_view'



