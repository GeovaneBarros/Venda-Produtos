from django.db.models.aggregates import Count
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from core.models import Produto, Modelo, Marca
from django.views import View
from core.forms import FilterProdutoForm
from django.db.models import Q
from django.core.paginator import Paginator
from django import template
from core.filters import ProdutoFilter

def filtragem(form, lista):
    if form.is_valid():
        marca_name = form['marca'].value()
        modelo_name =  form['modelo'].value()
        price_min = form['precoMin'].value()
        price_max = form['precoMax'].value()
        ano_min = form['anoMin'].value()
        ano_max = form['anoMax'].value()

        modelos = Modelo.objects.all()
        marcas = Marca.objects.all()

        if  price_min !='' and price_min is not None:
            lista = lista.filter(preco__gte=price_min)

        if  price_max !='' and price_max is not None:
            lista = lista.filter(preco__lte=price_max)
        
        if  ano_min !='' and ano_min is not None:
            lista = lista.filter(ano__gte=ano_min)

        if  ano_max !='' and ano_max is not None:
            lista = lista.filter(ano__lte=ano_max)

        if marca_name != '' and marca_name is not None:
            marcas = marcas.filter(marca__iexact=marca_name)
            modelos = modelos.filter(marca__in=marcas)
            lista = lista.filter(modelo__in=modelos)
            
        if modelo_name != '' and modelo_name is not None:
            modelos = modelos.filter(modelo__iexact=modelo_name)
            lista = lista.filter(modelo__in=modelos)
    return lista

def excluirPageUrl(query):
    cont = 0
    # Formatação para paginação
    if query.find('page') != -1:
        for i in query:
            if i == '&':
                break
            cont = cont + 1
    query = query[cont:]

    return query


class ProdutoList(ListView):
    template_name = 'produto/list.html'    
    queryset = Produto.objects.all()
    paginate_by = 4
    model = Produto

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.urlencode()
        query = excluirPageUrl(query)
        form = FilterProdutoForm(self.request.GET)
        context['query'] = query
        context['filter'] = form
        return context
    
    def get_queryset(self):
        lista = super().get_queryset()
        form = FilterProdutoForm(self.request.GET)
        lista = filtragem(form,lista)
        return lista

class ProdutoMostVisitedView(ListView):
    template_name = 'produto/list.html'    
    queryset = Produto.objects.all().order_by('-visitas')
    paginate_by = 4
    model = Produto

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.urlencode()
        query = excluirPageUrl(query)
        form = FilterProdutoForm(self.request.GET)
        context['query'] = query
        context['filter'] = form
        return context
    
    def get_queryset(self):
        lista = super().get_queryset()
        form = FilterProdutoForm(self.request.GET)
        lista = filtragem(form,lista)
        return lista

class ProdutoDetail(DetailView):
    context_object_name = 'produto'
    queryset = Produto.objects.all()
    template_name = 'produto/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        produto = self.get_object()
        produtos = self.get_queryset()
        produtos = produtos.filter(Q(modelo=produto.modelo), ~Q(id=produto.id))[:4]

        context['produto'] = produto
        context['produtos'] = produtos
        return context



class ProdutoVisita(View):
    def get(self, request ,pk):
        obj = Produto.objects.get(id=pk)
        obj.visitas = obj.visitas + 1
        obj.save()
        return redirect('produto_detail', pk)


class ProdutoIndex(TemplateView):
    template_name = 'produto/index.html'
