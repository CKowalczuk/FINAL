from django import forms
from .models import  Pregunta, Respuesta, PreguntasRespondidas
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, get_user_model
from django.forms.models import inlineformset_factory




User = get_user_model()
RespuestaFormset = inlineformset_factory(Pregunta, Respuesta, fields=('correcta', 'consigna',),can_delete_extra=False)

class RegistroFormulario(UserCreationForm):
	email = forms.EmailField(required=True)
	first_name = forms.CharField(required=True)
	last_name = forms.CharField(required=True)

	class Meta:
		model = User 
		fields = [
			'first_name',
			'last_name',
			'username',
			'email',
			'password1',
			'password2'
		]

class UsuarioLoginFormulario(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)


	def clean(self, *args, **kwargs):
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")

		if username and password:
			user = authenticate(username=username, password=password)
			if not user:
				raise forms.ValidationError("Usuario Inexistente")
			if not user.check_password(password):
				raise forms.ValidationError("Password incorrecto")
			if not user.is_active:
				raise forms.ValidationError("Usuario Inactivo")

		return super(UsuarioLoginFormulario, self).clean(*args, **kwargs)



class ElegirInlineFormset(forms.BaseInlineFormSet):
	
	def clean(self):



		if respuesta_pk == None:
			raise forms.ValidationError("DEBE SELECCIONAR UNA RESPUESTA")




		respuesta_correcta = 0
		for formulario in self.forms:
			
			if not formulario.is_valid():
				return

			if formulario.cleaned_data and formulario.cleaned_data.get('correcta') is True:
				respuesta_correcta += 1

		try:
			assert respuesta_correcta == Pregunta.PERMITIDAS
		except AssertionError:
			raise forms.ValidationError('Solo debe marcar una respuesta como correcta')



