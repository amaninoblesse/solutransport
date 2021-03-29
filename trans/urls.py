"""graphe URL Configuration

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

app_name='trans'
urlpatterns = [
    path('index/', views.index,name='index'),
    path('home/', views.home,name='home'),
    path('acceuil/', views.home1,name='acceuil'),
    path('client/', views.home2,name='client'),
    path('redirection/', views.redirection,name='redirection'),
    path('choix_client/', views.choix_client,name='choix_client'),
    path('vocal_form/', views.vocal_form,name='vocal_form'),
    path('client_deux/', views.client_deux,name='client_deux'),
    path('verify/', views.verify,name='verify'),
    path('liste_reservation/', views.liste_reservation,name='liste_reservation'),
    path('info_client/', views.info_client,name='info_client'),
    path('login/', views.login,name='login'),
    path('liste_client/', views.liste_client,name='liste_client'),
    path('liste_client/', views.liste_client,name='liste_client'),
    path('enregistrement/', views.enregistrement,name='enregistrement'),
    path('boss_login/', views.boss_login,name='boss_login'),
    path('register/', views.register,name='register'),
    path('donnee/', views.donnee,name='donnee'),
    path('donnee_client/', views.donnee_client,name='donnee_client'),


    
]
