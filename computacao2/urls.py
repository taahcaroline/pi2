from django.urls import path
from computacao2 import views


urlpatterns = [
    path('', views.home, name='meuapp-home'),
    path('sobre/', views.sobre, name='sobre'),
    path('nomeproduto/', views.produtotitle, name='nomeproduto'),
    path('produtocad/', views.produtocad, name='produtocad'),
    path('fornecedorcad/', views.fornecedorcad, name='fornecedorcad'),
    path('clientecad/', views.clientecad, name='clientecad'),
    path('servicocad/', views.servicocad, name='servicocad'),
    path('meusfornecedores/', views.meusfornecedores, name='meusfornecedores'),
    path('demandas/', views.demandas, name='demandas'),
    path('editarservico/', views.editdemandas, name='editarservico'),
    path('editarservico/<int:servicos_pk>/', views.editdemandas, name='editarservico'),
    path('deletarservico/<int:servicos_pk>/', views.demandasdelete, name='deletarservico'),
    path('clientescadastrados/', views.listaclientes, name='clientes'),
    path('editarcliente/', views.editclientes, name='editarcliente'),
    path('editarcliente/<int:cliente_pk>/', views.editclientes, name='editarcliente'),
    path('deletarcliente/<int:cliente_pk>/', views.demandasdelete, name='deletarcliente'),
]
