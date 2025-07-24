from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Usuario, Produto
from .forms import ProdutoForm

def usuario_required(view_func):
    def wrapper(request, *args, **kwargs):
        usuario_id = request.session.get('usuario_id')
        if not usuario_id:
            messages.error(request, 'Você precisa estar logado para acessar esta página.')
            return redirect('login')
        try:
            request.current_usuario = Usuario.objects.get(pk=usuario_id)
        except Usuario.DoesNotExist:
            messages.error(request, 'Sessão inválida. Por favor, faça login novamente.')
            if 'usuario_id' in request.session:
                del request.session['usuario_id']
            return redirect('login')
        return view_func(request, *args, **kwargs)
    return wrapper

def home(request):
    return render(request, 'home.html')

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        login = request.POST.get('login')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if senha == confirmar_senha:
            if not Usuario.objects.filter(login=login).exists():
                usuario = Usuario.objects.create(nome=nome, email=email, login=login, senha=senha)
                request.session['usuario_id'] = usuario.id 
                messages.success(request, 'Cadastro realizado com sucesso!')
                return redirect('cadastro_success')
            else:
                messages.error(request, 'Login já existente. Por favor, escolha outro.')
        else:
            messages.error(request, 'As senhas não coincidem.')
    return render(request, 'cadastro.html')

def cadastro_success(request):
    usuario = None
    usuario_logado_id = request.session.get('usuario_id')
    if usuario_logado_id:
        try:
            usuario = Usuario.objects.get(pk=usuario_logado_id)
        except Usuario.DoesNotExist:
            if 'usuario_id' in request.session:
                del request.session['usuario_id']
            
    context = {
        'usuario': usuario
    }
    return render(request, 'cadastro_success.html', context)

def login_view(request):
    if request.method == 'POST':
        login_input = request.POST.get('login')
        senha = request.POST.get('senha')

        try:
            usuario = Usuario.objects.get(login=login_input)
            if usuario.senha == senha:
                request.session['usuario_id'] = usuario.id
                messages.success(request, 'Login realizado com sucesso!')
                return redirect('cadastro_success')
            else:
                messages.error(request, 'Senha incorreta.')
        except Usuario.DoesNotExist:
            messages.error(request, 'Login não encontrado.')
    return render(request, 'login.html')

def logout_view(request):
    if 'usuario_id' in request.session:
        del request.session['usuario_id']
    messages.info(request, 'Você foi desconectado.')
    return redirect('home')

@usuario_required
def lista_produtos(request):
    produtos = Produto.objects.filter(usuario=request.current_usuario) 
    context = {
        'produtos': produtos
    }
    return render(request, 'lista_produtos.html', context)

@usuario_required
def adicionar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            produto = form.save(commit=False)
            produto.usuario = request.current_usuario
            produto.save()
            messages.success(request, 'Produto adicionado com sucesso!')
            return redirect('lista_produtos')
        else:
            messages.error(request, 'Ocorreu um erro ao adicionar o produto. Verifique os dados.')
    else:
        form = ProdutoForm()
    
    context = {
        'form': form
    }
    return render(request, 'adicionar_produto.html', context)

@usuario_required
def editar_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if produto.usuario != request.current_usuario:
        messages.error(request, 'Você não tem permissão para editar este produto.')
        return redirect('lista_produtos')
        
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto atualizado com sucesso!')
            return redirect('lista_produtos')
        else:
            messages.error(request, 'Ocorreu um erro ao atualizar o produto. Verifique os dados.')
    else:
        form = ProdutoForm(instance=produto)
    
    context = {
        'form': form,
        'produto': produto
    }
    return render(request, 'editar_produto.html', context)

@usuario_required
def excluir_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if produto.usuario != request.current_usuario:
        messages.error(request, 'Você não tem permissão para excluir este produto.')
        return redirect('lista_produtos')

    if request.method == 'POST':
        produto.delete()
        messages.success(request, 'Produto excluído com sucesso!')
        return redirect('lista_produtos')
    
    return render(request, 'confirmar_exclusao.html', {'produto': produto})