from django.shortcuts import render
from .models import Cadastro, Categoria


def listar_usuarios(request):

    lista_categorias = Categoria.objects.all()
    listar_usuarios = Cadastro.objects.all()


    return render(request, 'index.html')

