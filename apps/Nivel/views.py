from django.shortcuts import render
from django.http import HttpResponse
from .models import Preguntas 
from django.contrib.auth.decorators	import login_required
from django.contrib.auth.mixins		import LoginRequiredMixin
from django.views.generic			import ListView


# @login_required
# def nivel(request):
#     template_name ='Nivel_1.html'
#     lista_de_preguntas = Preguntas.objects.filter(id=2)
#     ctx = {
#     'preguntas': lista_de_preguntas,
#     }

#     return render(request, template_name, ctx)


class Nivel(LoginRequiredMixin,ListView):
	template_name ='Nivel_1.html'
	model = Preguntas
	context_object_name = 'Preguntas'

	# def get_queryset(self):
	# 	return Preguntas.objects.filter(nivel = 1)
