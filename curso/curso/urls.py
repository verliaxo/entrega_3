"""
URL configuration for curso project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from app_1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lista_profes/', lista_profes, name="lista_profes"),
    path('formulario_profes/',formulario_profes,name="formulario_profes"),
    path('buscar_profe/',buscar_profe,name="buscar_profe"),
    path('lista_alumnos/', lista_alumnos, name="lista_alumnos"),
    path('formulario_alumnos/',formulario_alumnos,name="formulario_alumnos"),
    path('lista_entregas/', lista_entregas, name="lista_entregas"),
    path('formulario_entregas/',formulario_entregas,name="formulario_entregas"),    
]
