
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', include('Inicio.urls')),
    path('nivel/',include('Nivel.urls')),
    path('Resultados/', include('Resultados.urls')),
]
