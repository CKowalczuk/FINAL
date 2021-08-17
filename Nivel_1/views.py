from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Nivel_1(request):
    return render(request, 'Nivel_1.html', {})
