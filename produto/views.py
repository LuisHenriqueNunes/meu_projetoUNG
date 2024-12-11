from django.shortcuts import render

from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto
from .forms import ProdutoForm 

def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produto/listar.html')

from django.shortcuts import render
from .models import Produto

def detalhes_produto(request, pk):
    produto = Produto.objects.get(pk=pk)
    return render(request, 'produto/detalhes.html',{'produto': produto})

def criar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')
    else:
        form = ProdutoForm()
    return render(request, 'produto/criar.html', {'form': form})

def editar_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'produto/editar.html', {'form': form})

def deletar_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        produto.delete()
        return redirect('listar_produto')
    return render(request, 'produto/deletar.html', {'produto':produto})

from django.shortcuts import render

# Defina a função produto_list
def produto_list(request):
    return render(request, 'produto/produto_listar.html')