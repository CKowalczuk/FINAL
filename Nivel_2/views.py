from django.shortcuts import render
from django.http import HttpResponse

def Nivel_2(request):
    return render(request, 'Nivel_2.html', {})