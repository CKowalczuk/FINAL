
from django.contrib 			import admin
from django.urls 				import path, include
from . 							import views
from django.contrib.auth	 	import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', include('apps.Inicio.urls')),
    path('nivel/',include('apps.Nivel.urls')),
    path('Resultados/', include('apps.Resultados.urls')),
    path('', views.inicio, name='principal'),
    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name = "login"),
    path('logout/', auth_views.logout_then_login, name = "logout"),
]
