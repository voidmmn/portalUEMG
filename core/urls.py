from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('acesso.urls')),  # Inclui as URLs da aplicação 'conta'
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

