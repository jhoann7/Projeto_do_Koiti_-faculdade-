from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuario
from django.shortcuts import redirect


def home(request):
    if request.method == "POST":
        return render(request, 'home.html')
    else:
        # Se for um POST para a rota home, redireciona para o cadastro
        return redirect('/cadastro/')

def cadastro(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        login = request.POST.get("login")
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        confirmar = request.POST.get("confirmar_senha")

        if senha != confirmar:
            return HttpResponse("As senhas não coincidem!")

        Usuario.objects.create(nome=nome, login=login, email=email, senha=senha)
        return redirect('/login/')  # Redireciona após cadastro
    return render(request, "cadastro.html")

def login_view(request):
    if request.method == "POST":
        login = request.POST.get("login")
        senha = request.POST.get("senha")

        try:
            usuario = Usuario.objects.get(login=login, senha=senha)
            return HttpResponse(f"Bem-vindo, {usuario.nome}!")
        except Usuario.DoesNotExist:
            return HttpResponse("Login ou senha incorretos.")

    return render(request, "login.html")