from django.contrib.auth.models import User
from django.shortcuts           import render


def inicio(request):
	template_name= "inicio.html"

# manejado por ORM
	# u = User.objects.create(username="usuario",first_name="Invitado1" )
	# print(User.objects.all())
	# u.save()

	ctx = {

	}
	return render(request,template_name, ctx)


