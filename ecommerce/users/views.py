from django.shortcuts import render

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                
                context = {'message':f'Bienvenido {username}!! :D'}
                return render(request, 'index.html', context = context)

        form = AuthenticationForm()
        return render(request, 'users/login.html', {'error': 'Formulário inválido', 'form': form})

    elif request.method == 'GET':
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        form = UserCreationForm()
        return render(request, 'users/register.html', {'form': form})
