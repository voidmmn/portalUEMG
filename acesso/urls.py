# conta/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views  # Importa as views da aplicação 'conta'

urlpatterns = [
    # Exemplo de uma URL para a página inicial da aplicação 'conta'
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('cadastro/', views.cadastro_view, name='cadastro'),
]
