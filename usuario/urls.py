from django.urls import path
from .views import listar_usuarios



app_name = 'usuarios'

urlpatterns = [

    path('usuarios/<slug_categoria>/', listar_usuarios,
    name='listar_usuarios_por_categoria'),
    path('usuarios/', listar_usuarios, name='listar_usuarios'),
]