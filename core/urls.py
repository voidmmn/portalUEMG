from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('acesso.urls')),  # Inclui as URLs da aplicação 'conta'
]

