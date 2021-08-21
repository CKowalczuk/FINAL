from django.shortcuts import render
from django.http import HttpResponse
from .models import Preguntas 

def nivel(request):
    template_name ='Nivel_1.html'
    lista_de_preguntas = Preguntas.objects.filter(id=2)
    ctx = {
    'preguntas': lista_de_preguntas,
    }

    return render(request, template_name, ctx)
2