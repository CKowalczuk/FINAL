from django.shortcuts 			import render
from django.contrib.auth.models import User

from .forms import RegistrarUsuario
from .models import Usuario

def nuevo_usuario(request):
	template_name = "registrarse.html"
	
	if request.method == "POST":
		apodo = request.POST.get("apodo",None)
		passw = request.POST.get("password")
		a = Usuario.objects.create(username=apodo, password=passw, nivel=1 )

	ctx = {
		'form': RegistrarUsuario()


	}
	return render(request,template_name, ctx)