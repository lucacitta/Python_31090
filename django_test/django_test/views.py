from django.http import HttpResponse
from datetime import datetime

from django.shortcuts import render

def saludo(request):
    return HttpResponse('Hola Mundo!!')

def canelones(request):
    return HttpResponse('Canelones de carne')

def dia_de_hoy(request):
    hoy = datetime.today().date()
    return HttpResponse(f'Hoy es {hoy}')

def saludo_con_nombre(request, nombre):
    return HttpResponse(f'Hola queridisimo {nombre}')

def año_de_nacimiento(request, edad):
    año_actual = datetime.today().year
    nacimiento = año_actual - edad
    return HttpResponse(f'Naciste en el año {nacimiento}')

def plantilla(request):
    return render(request, 'plantilla.html', context={})