"""
URL configuration for Tutorial1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from tutorial.views import submit_form, tutorial, thank_you,webdev,basic_coding,ai_ml,home,about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', tutorial, name='tutorial'),
    path('register/submit_form/', submit_form, name='submit_form'),
    path('thank-you/',thank_you,name='thank_you'),
    path('register/web-dev/',webdev,name='webdev'),
    path('register/ai-ml/',ai_ml,name='ai_ml'),
    path('register/basic-coding/',basic_coding,name='basic_coding'),
    path('',home,name='home'),
    path('register/about/',about,name='about')
]
