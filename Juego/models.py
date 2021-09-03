from django.db 					import models
from django.conf 				import settings
from django.contrib.auth.models import User
import random


# para cargar las preguntas 
class Pregunta(models.Model):

	PERMITIDAS = 1
	consigna = models.CharField(max_length=255)
	puntaje = models.DecimalField(verbose_name='Puntaje', default=0, decimal_places=2, max_digits=10)

	def __str__(self):
		return self.consigna 

# para cargar las respuestas, la fk Pregunta tiene (CANT_RESPUESTAS) respuestas
# posibles, se marca True la correcta

class Respuesta(models.Model):

	CANT_RESPUESTAS = 3
	pregunta = models.ForeignKey(Pregunta, related_name='opciones', on_delete=models.CASCADE)
	correcta = models.BooleanField(verbose_name='Tildar como correcta', default=False, null=False)
	consigna = models.CharField(max_length=255)


	def __str__(self):
		return self.consigna


class JuegoUsuario(models.Model):
	CANT_PREG_TEST = 30

	usuario = models.OneToOneField(User, on_delete=models.CASCADE)
	puntaje_total = models.DecimalField(verbose_name='Puntaje Total', default=0, decimal_places=2, max_digits=10)

	def __str__(self):
		return self.usuario
	
	def crear_intentos(self, pregunta):
		intento = PreguntasRespondidas(pregunta=pregunta, juegoUser=self)
		intento.save()

	def renovar_preguntas(self):

# almacena las id de las preguntas ya respondidas
		respondidas = PreguntasRespondidas.objects.filter(juegoUser=self).values_list('pregunta__pk', flat=True)
		if len(respondidas) >= JuegoUsuario.CANT_PREG_TEST:
			return None

# no permitir que se repitan las preguntas_restantes
# pk__in es una lista que contiene las id de las preguntas ya respondidas
		preguntas_restantes = Pregunta.objects.exclude(pk__in=respondidas)

# para permitir que se repitan las preguntas descomentar la siguientes 2 linea

		if not preguntas_restantes.exists():
		 	return None
		return random.choice(preguntas_restantes)

# Verifica que la pregunta no fue respondida
	def validar_intento(self, pregunta_respondida, respuesta_seleccionada):
		if pregunta_respondida.pregunta_id != respuesta_seleccionada.pregunta_id:
			return

		pregunta_respondida.respuesta_seleccionada = respuesta_seleccionada
		if respuesta_seleccionada.correcta is True:
			pregunta_respondida.correcta = True
			pregunta_respondida.puntaje_obtenido = respuesta_seleccionada.pregunta.puntaje
			pregunta_respondida.respuesta = respuesta_seleccionada

		else:
			pregunta_respondida.respuesta = respuesta_seleccionada

		pregunta_respondida.save()

		self.actualizar_puntaje()

	def actualizar_puntaje(self):
		puntaje_actualizado = self.intentos.filter(correcta=True).aggregate(
			models.Sum('puntaje_obtenido'))['puntaje_obtenido__sum']

		self.puntaje_total = puntaje_actualizado
		self.save()

class PreguntasRespondidas(models.Model):
	juegoUser = models.ForeignKey(JuegoUsuario, on_delete=models.CASCADE, related_name='intentos')
	pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
	respuesta = models.ForeignKey(Respuesta, on_delete=models.CASCADE, null=True)
	correcta  = models.BooleanField(verbose_name='¿Es esta la respuesta correcta?', default=False, null=False)
	puntaje_obtenido = models.DecimalField(verbose_name='Puntaje Obtenido', default=0, decimal_places=2, max_digits=10)
