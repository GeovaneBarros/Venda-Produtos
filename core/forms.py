from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Produto, Modelo, Admin, Marca
from django.contrib.auth.forms import UserCreationForm
from django import forms

class CadastroAdminForm(ModelForm):
    class Meta:
        model = Admin
        fields = ['nome', 'sobrenome']

class CadastroUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CadastroUserForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']     
        widgets = {
            'username':forms.EmailInput(attrs = {'class':'form-control'})     
        } 

class CadastroProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = ['ano','km','cor','caracteristicas', 'tipo', 'capa', 'preco']
        labels = {
            'km': ('Quilometragem'),
        }

class CadastroMarcaForm(ModelForm):
    class Meta:
        model = Marca
        fields = ['marca']
        
class CadastroModeloForm(ModelForm):
    class Meta:
        model = Modelo
        fields = ['modelo']