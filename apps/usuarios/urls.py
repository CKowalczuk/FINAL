from django.urls 	import path
from . 				import views

urlpatterns = [
    path('', views.nuevo_usuario, name='registrarse'),
]
