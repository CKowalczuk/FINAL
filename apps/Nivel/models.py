from django.db import models

class Preguntas(models.Model):

	pregunta = models.CharField(max_length=50)
	rta1 = models.CharField(max_length=50)
	rta1_v = models.BooleanField(default=False)
	rta2 = models.CharField(max_length=50)
	rta2_v = models.BooleanField(default=False)
	rta3 = models.CharField(max_length=50)
	rta3_v = models.BooleanField(default=False)
	categoria = models.CharField(max_length=50)
	nivel = models.IntegerField(default=1)

	class Meta:
		db_table = 'Preguntas'

	def __str__(self):
		return self.pregunta
