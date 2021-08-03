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


class FilterProdutoForm(forms.Form): 
    marca = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder':'Marca'}), label='')
    modelo = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder':'Modelo'}), label='')
    precoMin = forms.DecimalField(required=False, widget=forms.NumberInput(attrs={'placeholder':'Preço de'}), label='')
    precoMax = forms.DecimalField(required=False, widget=forms.NumberInput(attrs={'placeholder':'Até'}), label='')
    anoMin = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'placeholder':'Do ano'}), label='')
    anoMax = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'placeholder':'Até'}), label='')


class CreateMarcaForm(ModelForm):
    class Meta:
        model = Marca
        fields = '__all__'

class CreateModeloForm(ModelForm):
    class Meta:
        model = Modelo
        fields = '__all__'
        exclude = ['marca']

class CreateProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'
        exclude = ['modelo']