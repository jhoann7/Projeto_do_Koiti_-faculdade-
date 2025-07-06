from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login_view, name='login'),
    path('produtos/', views.lista_produtos, name='lista_produtos'),
    # --- Nova URL para Adicionar Produto ---
    path('produtos/adicionar/', views.adicionar_produto, name='adicionar_produto'),
    path('produtos/editar/<int:pk>/', views.editar_produto, name='editar_produto'), # <int:pk> captura o ID como inteiro
    path('produtos/excluir/<int:pk>/', views.excluir_produto, name='excluir_produto'),
]