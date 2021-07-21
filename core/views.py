from django.shortcuts import render, redirect
from .forms import CadastroProdutoForm, CadastroModeloForm
from .models import Produto, Modelo
from django.views import generic, View
# Create your views here.

class ProdutoIndex(generic.ListView):
    template_name = 'produto/listar.html'
    context_object_name = 'todos_produtos'
    def get_queryset(self):
        return Produto.objects.all() 

class ProdutoDetail(generic.DetailView):
    context_object_name = 'produto'
    queryset = Produto.objects.all()
    template_name = 'produto/detail.html'

    def get_object(self):
        obj = super().get_object()
        return obj
class IndexView(View):
    template_name = 'base.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

        
class ProdutoForm(View):
    template_name = 'produto/adicionar.html'

    def get(self, request, *args, **kwargs):
        data = {}
        data['form_modelo'] = CadastroModeloForm
        data['form_produto'] = CadastroProdutoForm
        return render(request, self.template_name, data)

    def post(self, request, *args, **kwargs):
        form = CadastroModeloForm(request.POST or None)
        nome_modelo = form['modelo'].value()
        nome_marca = form['marca'].value()
        if form.is_valid():

            # Verificando se o Modelo já existe ou criando um novo
            modelo, created = Modelo.objects.get_or_create(modelo=nome_modelo, marca=nome_marca)
            
            form = CadastroProdutoForm(request.POST or None)
            if form.is_valid:

                # Adicionando informacoes a uma variavel do tipo produto para salvar no banco
                produto = Produto()
                produto.modelo = modelo
                produto.ano = form['ano'].value()
                produto.km = form['km'].value()
                produto.cor = form['cor'].value()
                produto.caracteristicas = form['caracteristicas'].value()

                # Salvnado no banco
                produto.save()
                
                # Retornando para listagem de todos os produtos
                return render(request, 'listar_produtos')
        return render(request, self.template_name, {'form': form})