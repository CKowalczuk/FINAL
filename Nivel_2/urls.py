from django.urls import path

from . import views

urlpatterns = [
    path('', views.Nivel_2, name='Nivel_2'),
]