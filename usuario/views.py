from django.shortcuts import render, get_object_or_404
from .models import Cadastro, Categoria


def listar_usuarios(request, slug_categoria=None):
    categoria = None
    lista_categorias = Categoria.objects.all()
    lista_usuarios = Cadastro.objects.filter(ativo=True)
    if slug_categoria:
        categoria = get_object_or_404(Categoria, slug=slug_categoria)
        lista_produtos = Cadastro.objects.filter(categoria=categoria)

    contexto = {
        'categoria': categoria,
        'lista_categorias': lista_categorias,
        'lista_usuarios': lista_usuarios,
     }
    return render(request, 'userside.html')

