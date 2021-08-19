# from django.contrib.auth.models import User
# from django.shortcuts           import render


def inicio(request):
	template_name="base.html"
	return render(request,template_name)


from django.shortcuts import render
from django.http import HttpResponse
from .models import Preguntas

def nivel(request):
    template_name ='Nivel_1.html'
    lista_de_preguntas = Preguntas.object.all()
    ctx = {
    'preguntas': lista_de_preguntas,
    }

    return render(request, template_name, ctx)