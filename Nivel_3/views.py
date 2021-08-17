from django.shortcuts import render
from django.http import HttpResponse

def Nivel_3(request):
    return render(request, 'Nivel_3.html', {})
    