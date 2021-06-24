from django.contrib import admin
from .models import Cadastro, Categoria


@admin.register(Cadastro)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome','genero', 'etnia', 'deficiencia', 'estado', 'cidade', 'curso',
                    'periodo', 'email', 'linkedIn', 'site', 'pessoal', 'residencial', 'outro_tel',
                    'exp', 'atv', 'var1','porc1', 'var2', 'porc2', 'var3','porc3', 'var4', 'porc4',
                    'idi1','porc5', 'idi2','porc6', 'idi3','porc7', 'idi4', 'porc8',
                    'enfu', 'enme', 'bach', 'mes', 'dout', 'arint', 'salario', 'objpe', 'objpro',
                    'slug', 'criado', 'modificado', 'ativo']

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome','slug', 'criado', 'modificado']
