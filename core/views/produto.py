from django.shortcuts import render, redirect, reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from core.models import Produto, Modelo, Marca
from django.views import View
from core.filters import ProdutoFilter
from core.forms import FilterProdutoForm

class ProdutoList(View):
    template_name = 'produto/list.html'    

    def get(self, request):
        data = {}
        form = FilterProdutoForm(request.GET)
        lista = Produto.objects.all()

        if form.is_valid():
            marca_name = form['marca'].value()
            modelo_name =  form['modelo'].value()
            price_min = form['precoMin'].value()
            price_max = form['precoMax'].value()

            modelos = Modelo.objects.all()
            marcas = Marca.objects.all()

            if  price_min !='' and price_min is not None:
                lista = lista.filter(preco__gte=price_min)

            if  price_max !='' and price_max is not None:
                lista = lista.filter(preco__lte=price_max)

            if marca_name != '' and marca_name is not None:
                marcas = marcas.filter(marca__iexact=marca_name)
                modelos = modelos.filter(marca__in=marcas)
                lista = lista.filter(modelo__in=modelos)
                
            if modelo_name != '' and modelo_name is not None:
                modelos = modelos.filter(modelo__iexact=modelo_name)
                lista = lista.filter(modelo__in=modelos)
            
        data['list_produtos'] = lista
        data['filter'] = FilterProdutoForm
        return render(request, self.template_name, data)



class ProdutoDetail(DetailView):
    context_object_name = 'produto'
    queryset = Produto.objects.all()
    template_name = 'produto/detail.html'

    def get_object(self):
        obj = super().get_object()
        return obj


class ProdutoIndex(View):
    template_name = 'produto/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)