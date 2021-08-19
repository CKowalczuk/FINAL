from django.db import models

class Preguntas(models.Model):

	pregunta = models.CharField(max_length=255)
	respuestaCorr = models.CharField(max_length=255)
	rtaInc1 = models.CharField(max_length=255)
	rtaInc2 = models.CharField(max_length=255)
	categoria = models.CharField(max_length=255)
	nivel = models.IntegerField()

	class Meta:
		db_table = 'Preguntas'

	def __str__(self):
		return self.pregunta

