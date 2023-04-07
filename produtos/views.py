from django.shortcuts import render


def cadastrar_produto(request):
    if request.method == 'GET':
        return render(request, 'cadastrar_produto.html')
    elif request.method == 'POST':
        pass


def home(request):
    return render(request, 'home.html')
