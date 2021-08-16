from django.urls import path

from . import views

urlpatterns = [
    path('', views.Nivel_1, name='Nivel_1'),
]