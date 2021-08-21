from django.urls import path

from . import views

urlpatterns = [
    path('', views.Resultados, name='Resultados'),
]