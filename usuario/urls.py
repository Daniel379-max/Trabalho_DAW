from django.urls import path
from .views import listar_usuarios



app_name = 'usuarios'

urlpatterns = [

    path('produtos/<slug_categoria>/', listar_usuarios,
name='listar_produtos_por_categoria'),
    path('produtos/', listar_usuarios, name='listar_produtos'),
]