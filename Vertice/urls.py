from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # Painel de Administrador
    path('admin/', admin.site.urls),
    
    # Index
    path('', include('core.urls')),
    
    # Gerenciamento de Estoque
    path('estoque/', include('estoque.urls')),
    
    # Gerenciamento de Funcionário
    path('gestao/', include('gestao.urls')),
    
    # Vendas e Relatórios
    path('venda/', include('venda.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
