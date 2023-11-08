"""APITESCHI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from api.views import Home,Login_p,servicios,personas,Acerca,tabla_personas,exportar_personas_csv


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',Home.as_view(),name='index'),
    path('login_p/',Login_p.as_view(),name='Login_p'),
    path('servicios/',servicios.as_view(),name='servicios'),
    path('Acerca/',Acerca.as_view(),name='Acerca'),
    path('personas/',personas.as_view(),name='personas'),
    path('tabla-personas/', tabla_personas, name='tabla_personas'),
    path('exportar-csv/', exportar_personas_csv, name='exportar_personas_csv'),
    
         
]

