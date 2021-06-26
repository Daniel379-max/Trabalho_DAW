from django.urls import path, include
from .views import listar_usuarios
from django.contrib import admin


app_name = 'usuarios'

urlpatterns = [

    path('usuarios/<slug_categoria>/', listar_usuarios,
    name='listar_usuarios_por_categoria'),
    path('usuarios/', listar_usuarios, name='listar_usuarios'),
]