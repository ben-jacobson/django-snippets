"""auth_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from signin import views
#from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #path('', auth_views.LoginView.as_view(template_name='home.html'), name="home_page"), As a shortcut, you can simply call the view directly, rather than defining it in Views.py
    path('', views.home_page.as_view(), name="home_page"), # I prefer this since it's a little more verbose

    path('superheroes/', views.superhero_listView.as_view(), name="superhero_listview"),
    path('superheroes/<int:pk>/', views.superhero_detailView.as_view(), name="superhero_detailview"),
]




