from django.contrib import admin

from .models import Pregunta, Respuesta, PreguntasRespondidas, JuegoUsuario

from .forms import ElegirInlineFormset

from django.contrib.admin.models import LogEntry
from django.contrib.admin.models import DELETION
from django.utils.html import escape
from django.urls import reverse
from django.utils.safestring import mark_safe



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


@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    # to have a date-based drilldown navigation in the admin page
    date_hierarchy = 'action_time'

    # to filter the resultes by users, content types and action flags
    list_filter = [
        'user',
        'content_type',
        'action_flag'
    ]

    # when searching the user will be able to search in both object_repr and change_message
    search_fields = [
        'object_repr',
        'change_message'
    ]

    list_display = [
        'action_time',
        'user',
        'content_type',
        'action_flag',
    ]
    def has_add_permission(self, request):
    	return False
    def has_change_permission(self, request, obj=None):
    	return False
    def has_delete_permission(self, request, obj=None):
    	return False
    def has_view_permission(self, request, obj=None):
    	return request.user.is_superuser

    def object_link(self, obj):
    	if obj.action_flag == DELETION:
    		link = escape(obj.object_repr)
    	else:
    		ct = obj.content_type
    		link = '<a href="%s">%s</a>' % (reverse('admin:%s_%s_change' % (ct.app_label,ct.model), args=[obj.object_id]), escape(obj.object_repr),)
    		return mark_safe(link)





admin.site.register(PreguntasRespondidas)
admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(Respuesta)
admin.site.register(JuegoUsuario)