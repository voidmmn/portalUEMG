# conta/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views  # Importa as views da aplicação 'conta'

urlpatterns = [
    # Exemplo de uma URL para a página inicial da aplicação 'conta'
    path('', views.index, name='index'),
    path('', views.index, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('verificar/<str:token_verificacao>/', views.verificar_usuario, name='verificar_usuario'),
    path('perfil/', views.preencher_perfil_view, name='perfil'),
]
