from django.contrib import admin
from django.urls import path
from .views.manutencao import LogoutView, ProdutoAdminCreate, ProdutoAdminDetail, ProdutoAdminDelete, ProdutoAdminList, ProdutoAdminIndex, ProdutoAdminUpdate, LoginView, AdminCreate
from .views.produto import ProdutoList, ProdutoIndex, ProdutoDetail, ProdutoMostVisitedView, ProdutoVisita

urlpatterns = [


    # Urls para administrador de produtos
    path('manutencao', ProdutoAdminIndex.as_view(), name='produto_admin_index'),
    path('manutencao/list', ProdutoAdminList.as_view(), name='produto_admin_list'),
    path('manutencao/<int:pk>', ProdutoAdminDetail.as_view(), name='produto_admin_detail'),
    path('manutencao/<int:pk>/delete', ProdutoAdminDelete.as_view(), name='produto_admin_delete'),
    path('manutencao/<int:pk>/update', ProdutoAdminUpdate.as_view(), name='produto_admin_update'),
    path('manutencao/create', ProdutoAdminCreate.as_view(), name='produto_admin_create'),

    # Urls para novos administradores
    path('manutencao/admin/create', AdminCreate.as_view(), name='admin_create'),
       


    # Urls para usuario de produtos
    path('', ProdutoIndex.as_view(), name='produto_index'),
    path('produto/', ProdutoList.as_view(), name='produto_list'),
    path('mais_vistos', ProdutoMostVisitedView.as_view(), name='produto_most_views'),
    path('adicionar_visulizacao/<int:pk>', ProdutoVisita.as_view(), name='adicionar_view'),
    path('produto/<int:pk>/detalhe', ProdutoDetail.as_view(), name='produto_detail'),
    
    # Url login
    path('manutencao/login/', LoginView.as_view(), name='login_index'),
    path('manutencao/logout/', LogoutView.as_view(), name='logout'),
    
]
