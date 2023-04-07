from django.shortcuts import render, redirect
import re
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib import auth
from .models import Usuario



def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    elif request.method == 'POST':
        usuario = request.POST.get('usuario')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if len(senha) < 6:
            messages.add_message(request, constants.ERROR, 'Sua senha deve conter 6 ou mais caractertes')
            return redirect('/cadastro')

        if not senha == confirmar_senha:
            messages.add_message(request, constants.ERROR, 'As senhas não coincidem!')
            return redirect('/cadastro')

        if not re.search('[A-Z]', senha):
            messages.add_message(request, constants.ERROR, 'Sua senha não contem letras maiúsculas')
            return redirect('/cadastro')

        if not re.search('[a-z]', senha):
            messages.add_message(request, constants.ERROR, 'Sua senha não contem letras minúsculas')
            return redirect('/cadastro')

        if not re.search('[1-9]', senha):
            messages.add_message(request, constants.ERROR, 'Sua senha não contém números')
            return redirect('/cadastro')

        user = Usuario.objects.filter(usuario=usuario)

        if user:
            messages.add_message(request, constants.ERROR, 'Esse usuário já existe')
            return redirect('/cadastro')

        mail = Usuario.objects.filter(email=email)

        if mail:
            messages.add_message(request, constants.ERROR, 'Esse -email já está cadastrado')
            return redirect('/cadastro')

        try:
            user = Usuario(usuario=usuario, email=email)
            user.set_password(senha)
            user.save()
            messages.add_message(request, constants.SUCCESS, 'Cadastro realizado com sucesso !!!')
            return redirect('/cadastro')
        except Exception as e:
            e



def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')

        usuario = auth.authenticate(request, usuario=usuario, senha=senha)

        if not usuario:
            messages.add_message(request, constants.ERROR, 'Username ou senha inválidos !!!')
            return redirect('/login')
        else:
            # se o usuário existe no banco de dados, pe feita a autenticação do usuário abaixo
            auth.login(request, usuario)
            return redirect('/home')


def sair(request):
    auth.logout(request)
    return redirect('/login')





