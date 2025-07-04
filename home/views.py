from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario

# View principal que salva apenas nome
def home(request):
    if request.method == "GET":
        return render(request, 'home.html')
    else:
        nome = request.POST.get('nome')
        user = Usuario(nome=nome)
        user.save()
        return HttpResponse(nome)

def cadastro(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        login = request.POST.get("login")
        email = request.Post.get("login")
        senha = request.Post.get("senha")
        confirmar = request.Post.get("confirmar_senha")

        if senha != confirmar:
            return HttpResponse("As senhas não coincidem!")

        # salva no banco
        usuario = Usuario(nome=nome, login=login, senha=senha, email=email)
        usuario.save()

        return HttpResponse("Usuário cadastrado com sucesso!")
    return render(request, "cadastro.html")