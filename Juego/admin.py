from django.contrib import admin

from .models import Pregunta, Respuesta, PreguntasRespondidas, JuegoUsuario

from .forms import ElegirInlineFormset

class RespuestaInline(admin.TabularInline):
	model = Respuesta
	can_delete =False
	max_num = Respuesta.CANT_RESPUESTAS
	min_num = Respuesta.CANT_RESPUESTAS
	formset = ElegirInlineFormset

class PreguntaAdmin(admin.ModelAdmin):
	model = Pregunta
	inlines = (RespuestaInline, )
	list_display = ['consigna',]
	search_fields = ['consigna', 'preguntas__consigna']


class PreguntasRespondidasAdmin(admin.ModelAdmin):
	list_display = ['pregunta', 'respuesta', 'correcta', 'puntaje_obtenido']

	class Meta:
		model = PreguntasRespondidas


admin.site.register(PreguntasRespondidas)
admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(Respuesta)
admin.site.register(JuegoUsuario)