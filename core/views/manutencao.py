from django.shortcuts import render, redirect, reverse
from core.forms import CadastroAdminForm, CadastroUserForm, CreateMarcaForm, CreateModeloForm, CreateProdutoForm
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from core.models import Marca, Produto, Modelo
from django.views.generic.base import View, TemplateView
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class LoginView(View):
    template_name = 'manutencao/login/index.html'

    def get(self, request):
        if request.user.is_authenticated:
	        return render('manutencao/produto/index.html')
        return render(request, self.template_name)
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('produto_admin_index')
        messages.info(request, 'Email ou senha incorretos')


class LogoutView(View):
    def get(self, request):
        auth.logout(request)
        return redirect('produto_index')


@method_decorator(login_required, name='dispatch')
class AdminCreate(View):
    template_name = 'manutencao/admin/create.html'

    def get(self, request, *args, **kwargs):
        data = {}
        data['form_user'] = CadastroUserForm
        data['form_admin'] = CadastroAdminForm
        return render(request, self.template_name, data)

    def post(self, request, *args, **kwargs):
        form_user = CadastroUserForm(request.POST)
        form_admin = CadastroAdminForm(request.POST)
        if form_user.is_valid() and form_admin.is_valid():         
            user = form_user.save()
            user.save()

            admin = form_admin.save(commit = False)
            admin.user = user
            admin.save()
                
            auth.login(request, user)
            return redirect('produto_admin_index')
        
        data = {}
        data['form_user'] = CadastroUserForm
        data['form_admin'] = CadastroAdminForm
        return render(request, self.template_name, data)


@method_decorator(login_required, name='dispatch')
class ProdutoAdminIndex(TemplateView):
    template_name = 'manutencao/produto/index.html'

@method_decorator(login_required, name='dispatch')
class ProdutoAdminList(ListView):
    template_name = 'manutencao/produto/list.html'
    context_object_name = 'list_produto'

    def get_queryset(self):
        return Produto.objects.all()
    

@method_decorator(login_required, name='dispatch')
class ProdutoAdminDetail(DetailView):
    context_object_name = 'produto'
    queryset = Produto.objects.all()
    template_name = 'manutencao/produto/detail.html'

    def get_object(self):
        obj = super().get_object()
        return obj


@method_decorator(login_required, name='dispatch')
class ProdutoAdminDelete(DeleteView):
    model = Produto
    template_name = 'manutencao/produto/delete.html'
    success_url ="/manutencao"


@method_decorator(login_required, name='dispatch')
class ProdutoAdminCreate(View):
    template_name = 'manutencao/produto/create.html'

    def get(self, request, *args, **kwargs):
        data = {}
        data['form_modelo'] = CreateModeloForm
        data['form_marca'] = CreateMarcaForm
        data['form_produto'] = CreateProdutoForm

        return render(request, self.template_name, data)

    def post(self, request, *args, **kwargs):
        form = CreateMarcaForm(request.POST)

        if form.is_valid():
            nome_marca = form['marca'].value()
            marca, created = Marca.objects.get_or_create(marca=nome_marca)
            form = CreateModeloForm(request.POST)
            if form.is_valid():
                nome_modelo = form['modelo'].value()
                # Verificando se o Modelo já existe ou criando um novo
                modelo, created = Modelo.objects.get_or_create(modelo=nome_modelo, marca=marca)
                
                # Adicionando informacoes a uma variavel do tipo produto para salvar no banco
                form = CreateProdutoForm(request.POST, request.FILES)
                if form.is_valid():
                    produto = Produto()
                    produto.modelo = modelo
                    produto.ano = form['ano'].value()
                    produto.cilindrada = form['cilindrada'].value()
                    produto.km = form['km'].value()
                    produto.cor = form['cor'].value()
                    produto.caracteristicas = form['caracteristicas'].value()
                    img = form.cleaned_data.get("capa")
                    produto.capa = img
                    produto.tipo = form['tipo'].value()
                    produto.preco = form['preco'].value()
                    # Salvnado no banco
                    produto.save()
                    
                    # Retornando para listagem de todos os produtos
                    return redirect('produto_admin_list')
   
        data = {}
        data['form_modelo'] = CreateModeloForm
        data['form_marca'] = CreateMarcaForm
        data['form_produto'] = CreateProdutoForm


@method_decorator(login_required, name='dispatch')
class ProdutoAdminUpdate(UpdateView):
    model = Produto
    template_name = 'manutencao/produto/update.html'
    fields = ['ano', 'km', 'cor', 'caracteristicas', 'capa', 'preco', 'tipo','cilindrada']
    success_url = '/manutencao/list'