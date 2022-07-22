from django.contrib import admin
from django.urls import path
from ecommerce.views import saludo, segundo_template, template_con_lista

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('saludo/', saludo, name='saludo'),
    path('segundo_template/', segundo_template, name='segundo_template'),
    path('template_con_lista/', template_con_lista, name='template_con_lista')
]
