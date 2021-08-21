from django.shortcuts 			import render
from django.contrib.auth.models import User
from forms 						import RegistrationForm

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    model = User
    template_name = 'registrarse.html'