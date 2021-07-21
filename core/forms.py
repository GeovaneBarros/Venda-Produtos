from django.forms import ModelForm
from django import forms
from .models import Produto, Modelo

class CadastroProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = ['ano','km','cor','caracteristicas']
        labels = {
            'km': ('Quilometragem'),
        }

class CadastroModeloForm(ModelForm):
    class Meta:
        model = Modelo
        fields = ['modelo', 'marca']