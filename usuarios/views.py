from urllib import request
from django.shortcuts import render, redirect

def cadastro(request):

    if request.method == 'POST':
        nome = request.POST['nome']
        print('Usuário criado com sucesso')
        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')


def login(request):
    return render(request, 'usuarios/login.html')

def dashboard(request):
    pass

def logout(request):
    pass