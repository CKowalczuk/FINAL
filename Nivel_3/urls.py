from django.urls import path

from . import views

urlpatterns = [
    path('', views.Nivel_3, name='Nivel_3'),
]