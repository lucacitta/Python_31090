from django.contrib import admin
from django.urls import path

from django_test.views import saludo, canelones, dia_de_hoy, saludo_con_nombre, año_de_nacimiento, plantilla


urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo, name='view_de_saludo'),
    path('canelones/', canelones, name='canelones'),
    path('dia-de-hoy/', dia_de_hoy, name='dia_de_hoy'),
    path('saludo-con-nombre/<str:nombre>/', saludo_con_nombre, name='saludo_con_nombre'),
    path('nacimiento/<int:edad>/', año_de_nacimiento, name='nacimiento'),
    path('plantilla/', plantilla, name='plantilla')
]
