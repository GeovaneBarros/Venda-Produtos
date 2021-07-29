from django.db.models import fields
from django_filters import FilterSet, NumberFilter

from .models import *

class MarcaFilter(FilterSet):
    class Meta:
        model = Marca
        fields = ['marca']

class ProdutoFilter(FilterSet):
    class Meta:
        model = Produto
        fields = ['preco']