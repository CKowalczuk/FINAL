from django import forms
from .models import Usuario

class RegistrarUsuario(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ["apodo","password"]
        