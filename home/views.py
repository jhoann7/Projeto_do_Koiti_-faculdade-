from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from .models import Usuario, Produto
from django.shortcuts import redirect
from .forms import ProdutoForm



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

def lista_produtos(request):
    produtos = Produto.objects.all()
    context = {
        'produtos': produtos
    }
    return render(request, 'lista_produtos.html', context)

# --- Nova View para Adicionar Produto ---
def adicionar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save() # Salva o novo produto no banco de dados
            messages.success(request, 'Produto adicionado com sucesso!')
            return redirect('lista_produtos') # Redireciona para a lista de produtos
        else:
            messages.error(request, 'Ocorreu um erro ao adicionar o produto. Verifique os dados.')
    else: # Se o método for GET (para exibir o formulário vazio)
        form = ProdutoForm()
    
    context = {
        'form': form
    }
    return render(request, 'adicionar_produto.html', context)

def editar_produto(request, pk): # 'pk' é a chave primária do produto
    produto = get_object_or_404(Produto, pk=pk) # Tenta pegar o produto pelo ID ou retorna 404
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto) # Passa a instância do produto para preencher o formulário
        if form.is_valid():
            form.save() # Salva as alterações no produto existente
            messages.success(request, 'Produto atualizado com sucesso!')
            return redirect('lista_produtos')
        else:
            messages.error(request, 'Ocorreu um erro ao atualizar o produto. Verifique os dados.')
    else:
        form = ProdutoForm(instance=produto) # Preenche o formulário com os dados atuais do produto
    
    context = {
        'form': form,
        'produto': produto # Passa o produto para o template, útil para exibir o nome, por exemplo
    }
    return render(request, 'editar_produto.html', context)

# --- Nova View para Excluir Produto ---
def excluir_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk) # Tenta pegar o produto pelo ID ou retorna 404
    if request.method == 'POST':
        produto.delete() # Exclui o produto do banco de dados
        messages.success(request, 'Produto excluído com sucesso!')
        return redirect('lista_produtos')
    # Para requisições GET, podemos renderizar uma página de confirmação
    return render(request, 'confirmar_exclusao.html', {'produto': produto}) # Vamos criar este template
