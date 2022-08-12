from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from ecommerce.views import saludo, segundo_template, template_con_lista, index


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', index, name='index'),
    
    path('saludo/', saludo, name='saludo'),
    path('segundo-template/', segundo_template, name='segundo_template'),
    path('template-con-lista/', template_con_lista, name='template_con_lista'),
    path('articles/', include('blog.urls')),
    path('products/', include('products.urls')),
    path('users/', include('users.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
