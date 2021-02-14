"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('register-user/',views.register_user,name="register-user"),
    path('search-user/',views.search_user,name="search-user"),
    path('del-user/',views.del_user,name="del-user"),
    path('get-brand/',views.get_brand,name="get-brand"),


    # javascript validation 

    path('javascript-validation-page/',views.javascript_validation_page,name="javascript-validation-page"),
    
]
