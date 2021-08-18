from django.db import models


class Preguntas(models.Model):
	pregunta = models.CharField(max_length=255)
	respuesta = models.CharField(max_length=255)
	class Meta:
		db_table = 'Preguntas'

	def __str__(self):
		return self.pregunta
