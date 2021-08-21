from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
	apodo = models.CharField(max_length=50,null=True, blank=True)
	fecha_nacimiento = models.DateField(null=True, blank=True)
	nivel =  models.IntegerField(null=True, blank=True)

	class Meta:
		db_table = 'usuarios'
