# conta/urls.py
from django.urls import path
from . import views  # Importa as views da aplicação 'conta'

urlpatterns = [
    # Exemplo de uma URL para a página inicial da aplicação 'conta'
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('cadastro/', views.cadastro_view, name='cadastro'),
]
