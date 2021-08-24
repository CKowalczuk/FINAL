from django import forms
from .models import Preguntas

class ListarPreguntas(forms.ModelForm):
    class Meta:
        model = Preguntas
        r1=False
        r2=False
        r3=False
        fields = ["rta1","rta2","rta3", "rta1_v", "rta2_v","rta3_v"]
