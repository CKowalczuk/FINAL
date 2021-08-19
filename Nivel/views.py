from django.shortcuts import render
from django.http import HttpResponse
from Inicio.models import Preguntas

def nivel(request):
    template_name ='Nivel_1.html'
    # lista_de_preguntas = Preguntas.object.all()
    ctx = {
    'preguntas': Preguntas.object.all(),#lista_de_preguntas,
    }

    return render(request, template_name, ctx)
