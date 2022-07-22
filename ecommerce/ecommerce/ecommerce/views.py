from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

def saludo(request):
    return HttpResponse('Holis, segunda clase con Django')

def segundo_template(request):
    today = datetime.now().date
    context = {
        'name':'Luca',
        'last_name':'Citta Giordano',
        'today': today 
    }
    return render(request, 'template_2.html', context=context)

def template_con_lista(request):
    context = {
        'lista':['tomate', 'banana', 'naranja'],
    }
    return render(request, 'template_lista.html',context=context)

