from django.urls import path

from . import views

# app_name = 'Nivel'

urlpatterns = [
    # path('', views.nivel,name='Nivel'),
    path('', views.Nivel.as_view(),name='Nivel'),

]