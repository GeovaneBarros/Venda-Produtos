from django.contrib import admin
from django.urls import path
from core.views import ProdutoIndex, ProdutoDetail, ProdutoForm, IndexView
urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', IndexView.as_view(), name='base_view'),
    path('produtos', ProdutoIndex.as_view(), name='listar_produtos'),
    path('produto/add', ProdutoForm.as_view(), name='form_produto'),
    path('produto/<int:pk>/', ProdutoDetail.as_view(), name='detalhar_produto'),
    
]
