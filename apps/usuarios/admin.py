from django.contrib import admin
from .models import Usuario
# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
	list_display = ['id','username','nivel' ]

admin.site.register(Usuario,UsuarioAdmin)

