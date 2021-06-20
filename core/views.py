from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def para_empresa(request):
    return render(request, 'para_empresa.html')

def para_candidato(request):
    return render(request, 'para_candidato.html')

def contato(request):
    return render(request, 'contato.html')

def arrow(request):
    return render(request, 'arrow.html')

