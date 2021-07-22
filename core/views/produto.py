from django.shortcuts import render, redirect, reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from core.models import Produto, Modelo
from django.views import View

class ProdutoList(ListView):
    template_name = 'produto/list.html'
    context_object_name = 'list_produto'

    def get_queryset(self):
        return Produto.objects.all()

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