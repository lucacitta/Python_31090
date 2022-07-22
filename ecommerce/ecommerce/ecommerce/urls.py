from django.contrib import admin
from django.urls import path
from ecommerce.views import saludo, segundo_template

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('saludo/', saludo, name='saludo'),
    path('segundo_template/', segundo_template, name='segundo_template')
]
