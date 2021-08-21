
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', include('apps.Inicio.urls')),
    path('nivel/',include('apps.Nivel.urls')),
    path('Resultados/', include('apps.Resultados.urls')),
    path('', views.inicio),
]
