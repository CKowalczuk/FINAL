from django.shortcuts 			import render
from django.contrib.auth.models import User
from .models 					import Usuario
from django.urls				import reverse_lazy
from .forms import UserForm
from django.contrib.auth.forms 	import UserCreationForm
from django.shortcuts import redirect
# from .models import Usuario



def register(request):
    template_name = "registrarse.html"
    if request.method == 'POST':
    	form = UserForm(request.POST)
    	if form.is_valid():
    		form.save()
    	# apodo = request.POST.get("username",None)
    	# password1 = request.POST.get("password1",None)
    	# a = Usuario.objects.create(username=apodo, apodo=apodo, password=password1, nivel=1 )
    	return reverse_lazy("inicio")
    else:
    	ctx = {
    	'form' : UserForm()
        }

    return render(request, template_name, ctx)





# def nuevo_usuario(request):
# 	template_name = "registrarse.html"
	
# 	if request.method == "POST":
# 		apodo = request.POST.get("apodo",None)
# 		passw = request.POST.get("password")
# 		a = Usuario.objects.create(username=apodo, password=passw, nivel=1 )

# 	ctx = {
# 		'form': RegistrarUsuario()


# 	}
# 	return render(request,template_name, ctx)