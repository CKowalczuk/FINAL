from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import RegistroFormulario, UsuarioLoginFormulario
from .models import JuegoUsuario, Pregunta, PreguntasRespondidas




def inicio(request):
	template_name = 'inicio.html'
	context = {
		'bienvenido': 'Bienvenido'
	}
	return render(request, template_name, context)




# crea un registro con el usuario y el puntaje obtenido
def jugar(request):
	template_name = 'Juego/jugar.html'
	# no funnciona, se cambió el create por el get_or_create
	# JuegoUser = JuegoUsuario.objects.create(usuario=request.user)

	JuegoUser, created = JuegoUsuario.objects.get_or_create(usuario=request.user)

	if request.method == 'POST':
		preg_pk = request.POST.get('preg_pk')
		pregunta_respondida = JuegoUser.intentos.select_related('pregunta').get(pregunta__pk=preg_pk)
		respuesta_pk = request.POST.get('respuesta_pk')




# agregar excepción si no marca opcion---------------------------------------

		try:
			opcion_selecCionada = pregunta_respondida.pregunta.opciones.get(pk=respuesta_pk)
		except:
			raise UnboundLocalError("DEBE ELEGIR UNA RESPUESTA")


# agregar axcepción si no marca opcion---------------------------------------


		JuegoUser.validar_intento(pregunta_respondida, opcion_selecCionada)
		

		return redirect('resultado', pregunta_respondida.pk)

	else:
		pregunta = JuegoUser.renovar_preguntas()
		if pregunta is not None:
			JuegoUser.crear_intentos(pregunta)

		context = {
			'pregunta':pregunta
		}

	return render(request, template_name, context)





# toma el resultado y lo envía a resultados html para informar
# si es correcta o incorrecta

def resultado_pregunta(request, pregunta_respondida_pk):
	template_name = 'Juego/resultados.html'
	respondida = get_object_or_404(PreguntasRespondidas, pk=pregunta_respondida_pk)

	context = {
		'respondida':respondida
	}
	return render(request, template_name, context)





# cuenta los usuarios registrados y los ordena por la cantidad de puntos
def ranking(request):
	template_name = 'Juego/ranking.html'
	total_usuarios_juego = JuegoUsuario.objects.order_by('-puntaje_total')[:10]
	contador = total_usuarios_juego.count()

	context = {

		'usuario_juego':total_usuarios_juego,
		'cant_usuarios':contador
	}

	return render(request, template_name, context)




# login para usuarios registrados

def loginView(request):
	template_name = 'Usuario/login.html'
	titulo = 'login'
	form = UsuarioLoginFormulario(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		usuario = authenticate(username=username, password=password)
		login(request, usuario)
		return redirect('HomeUsuario')

	context = {
		'form':form,
		'titulo':titulo
	}

	return render(request, template_name, context)



def HomeUsuario(request):
	template_name = 'Usuario/base.html'
	context = {

	}
	
	return render(request, template_name, context)


def registro(request):
	template_name = 'Usuario/registro.html'
	titulo = 'Crear una Cuenta'
	if request.method == 'POST':
		form = RegistroFormulario(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
	else:
		form = RegistroFormulario()

	context = {

		'form':form,
		'titulo': titulo

	}

	return render(request, template_name, context)


def logout_vista(request):
	logout(request)
	return redirect('/')




# from django.db import models
# from django.contrib.auth.models import AbstractUser

# models
# class Usuario(AbstractUser):
# 	apodo = models.CharField(max_length=50,null=True, blank=True)
# 	fecha_nacimiento = models.DateField(null=True, blank=True)
# 	nivel =  models.IntegerField(null=True, blank=True)

# 	class Meta:
# 		db_table = 'usuarios'

