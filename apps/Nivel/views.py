
from django.shortcuts 				import render
from django.http 					import HttpResponse
from .models 						import Preguntas 
from django.contrib.auth.decorators	import login_required
from django.contrib.auth.mixins		import LoginRequiredMixin
from django.views.generic			import ListView
from .forms 						import ListarPreguntas



# @login_required
def nivel(request):
    template_name ='Nivel_1.html'
    for x in range(3):
    	lista_de_preguntas = Preguntas.objects.filter(pk=x-1)
    	
    	if request.method == "POST":
            rta1 = request.POST.get("rta1",None)
            rta2 = request.POST.get("rta2",None)
            rta3 = request.POST.get("rta3",None)
            print(self.objects.rta1_v)
            


    		# field_name = 'rta1_v'
    		# obj1 = Preguntas.objects.first()
    		# obj = Preguntas.objects.filter(pk=x)
    		# field_object = Preguntas._meta.get_field(field_name)
    		# field_value = getattr(obj, field_object.attname)
    		# print(rta1,field_value)

    	

    	# field_name1 = 'rta1_v'
    	# field_name2 = 'rta2_v'
    	# field_name3 = 'rta3_v'
    	# obj = Preguntas.objects.filter(pk=x-1)

    	# field_object1 = Preguntas._meta.get_field(field_name1)
    	# field_value1 = getattr(obj, field_object1.attname)

    	# field_object2 = Preguntas._meta.get_field(field_name2)
    	# field_value2 = getattr(obj, field_object2.attname)

    	# field_object3 = Preguntas._meta.get_field(field_name3)
    	# field_value3 = getattr(obj, field_object3.attname)
    	
    	# print(rta1,field_value1)
    	# print(rta2,field_value2)
    	# print(rta3,field_value3)
       	
	 #   	if rta1== "on" and Preguntas.rta1_v:
	 #   		print("------------------")
	 #    	print("Respuesta Correcta")
	 #    	print("------------------")
	 #    elif rta2 == "on" and Preguntas.rta2_v:
	 #    	print("------------------")
	 #    	print("Respuesta Correcta")
	 #    	print("------------------")
		# elif rta3 == "on" and Preguntas.rta3_v:
	 #    	print("------------------")
	 #    	print("Respuesta Correcta")
	 #    	print("------------------")


    ctx = {
       	'preguntas': lista_de_preguntas,
       	'form': ListarPreguntas(),
       	}

    return render(request, template_name, ctx)


# class Nivel(LoginRequiredMixin,ListView):
# 	template_name ='Nivel_1.html'
# 	model = Preguntas
# 	context_object_name = 'Preguntas'

	# def get_queryset(self):
	# 	return Preguntas.objects.filter(nivel = 1)

