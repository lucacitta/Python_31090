from django.contrib import admin
from django.urls import path
from ecommerce.views import saludo, segundo_template, template_con_lista
from products.views import create_product, list_products

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo, name='saludo'),
    path('segundo-template/', segundo_template, name='segundo_template'),
    path('template-con-lista/', template_con_lista, name='template_con_lista'),
    path('create-product/', create_product, name='create_product'),
    path('list-products/', list_products, name='list_products')
]
