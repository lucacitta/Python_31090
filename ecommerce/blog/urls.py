from django.urls import path
from blog.views import create_article

urlpatterns = [
    path('create-article/', create_article, name='create_article'),
]