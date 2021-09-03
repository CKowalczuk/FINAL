from django 					import forms
from .models 					import  Pregunta, Respuesta, PreguntasRespondidas
from django.contrib.auth.forms 	import UserCreationForm
from django.contrib.auth 		import authenticate, get_user_model
from django.forms.models 		import inlineformset_factory

User = get_user_model()
RespuestaFormset = inlineformset_factory(Pregunta, Respuesta, fields=('correcta', 'consigna',),can_delete_extra=False)

class RegistroFormulario(UserCreationForm):
	
	first_name = forms.CharField(label='Nombre',widget=forms.TextInput(attrs={"placeholder":"Ingrese su Nombre",'class':'form-control'}))
	last_name = forms.CharField(label='Apellido',widget=forms.TextInput(attrs={'class':'form-control',"placeholder":"Ingrese su Apellido"}))
	username = forms.CharField(label='Usuario',widget=forms.TextInput(attrs={'class':'form-control',"placeholder":"Elija un Apodo"}))
	password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
	password2 = forms.CharField(label='Reingrese Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
	
	class Meta:
		model = User 
		fields = [
			'username',
			'first_name',
			'last_name',
 			'password1',
			'password2'
		]

class UsuarioLoginFormulario(forms.Form):
	username = forms.CharField(label='Usuario',widget=forms.TextInput(attrs={'class':'form-control',"placeholder":"Ingrese su Apodo"}))
	password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))


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



