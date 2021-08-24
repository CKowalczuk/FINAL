from django import forms
from .models import Usuario

from django.contrib.auth.forms 	import UserCreationForm

class UserForm(UserCreationForm):
	first_name = forms.CharField()
	last_name = forms.CharField()
	email = forms.EmailField()

	class Meta:
		model = Usuario
		fields = ('first_name','last_name', 'username', 'email', 'password1' ,'password2' )





# class RegistrarUsuario(forms.ModelForm):
#     class Meta:
#         model = Usuario
#         fields = ["apodo","password"]
#         