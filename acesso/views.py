from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import CadastroUsuarioForm

def index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Verifica se o e-mail termina com @uemg.br
        if not username.endswith('@uemg.br'):
            messages.error(request, 'Por favor, utilize seu e-mail institucional da UEMG.')
            return render(request, 'acesso/login.html')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Substitua 'index' pelo nome da sua URL de destino após o login
        else:
            messages.error(request, 'Usuário ou senha inválidos')
            return render(request, 'acesso/login.html')

    return render(request, 'acesso/login.html')

def cadastro_view(request):
    if request.method == 'POST':
        form = CadastroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redireciona para a página de login após o cadastro bem-sucedido
    else:
        form = CadastroUsuarioForm()
    return render(request, 'acesso/cadastro.html', {'form': form})