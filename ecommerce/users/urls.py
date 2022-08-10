from django.urls import path
from users.views import login_request, register

urlpatterns = [
    path('login/', login_request, name='login'),
    path('register/', register, name='register'),
]