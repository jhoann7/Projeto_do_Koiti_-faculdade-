from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuario

def home(request):
    if request.method == "GET":
        return render(request, 'home.html')
    else:
        nome = request.POST.get('nome')
        return HttpResponse(f"Olá, {nome}!")

def cadastro(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        login = request.POST.get("login")
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        confirmar = request.POST.get("confirmar_senha")

        # Validações
        if senha != confirmar:
            return HttpResponse("As senhas não coincidem!")

        if Usuario.objects.filter(login=login).exists():
            return HttpResponse("Esse login já está em uso!")

        if Usuario.objects.filter(email=email).exists():
            return HttpResponse("Esse e-mail já está cadastrado!")

        # Salvar no banco
        usuario = Usuario(nome=nome, login=login, email=email, senha=senha)
        usuario.save()
        return redirect('/login/')

    return render(request, "cadastro.html")

def login_view(request):
    if request.method == "POST":
        login = request.POST.get("login")
        senha = request.POST.get("senha")

        try:
            usuario = Usuario.objects.get(login=login, senha=senha)
            return HttpResponse(f"Bem-vindo, {usuario.nome}!")
        except Usuario.DoesNotExist:
            return HttpResponse("Login ou senha incorretos!")

    return render(request, "login.html")