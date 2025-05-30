from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Pessoa
from .forms import PessoaForm
from django.contrib.auth.decorators import login_required


# View que lista todas as pessoas
@login_required
def index(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'pessoa/index.html', {'pessoas': pessoas})


# View que mostra detalhes de uma pessoa
@login_required
def detalha(request, id_pessoa):
    pessoa = get_object_or_404(Pessoa, id=id_pessoa)
    return render(request, 'pessoa/detalha.html', {'pessoa': pessoa})


# View para criar uma nova pessoa
@login_required
def create(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index-pessoa')
    else:
        form = PessoaForm()

    return render(request, 'pessoa/create.html', {'form': form})


# View para atualizar uma pessoa existente
@login_required
def update(request, id_pessoa):
    pessoa = get_object_or_404(Pessoa, id=id_pessoa)
    if request.method == 'POST':
        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()
            return redirect('index-pessoa')
    else:
        form = PessoaForm(instance=pessoa)

    return render(request, 'pessoa/update.html', {'form': form})


# View para deletar uma pessoa
@login_required
def delete(request, id_pessoa):
    pessoa = get_object_or_404(Pessoa, id=id_pessoa)
    if request.method == 'POST':
        pessoa.delete()
        return redirect('index-pessoa')
    return render(request, 'pessoa/delete.html', {'pessoa': pessoa})


# Exemplo de view simples (opcional)
def read(request):
    return HttpResponse("<h3>Aqui que lê!</h3>")