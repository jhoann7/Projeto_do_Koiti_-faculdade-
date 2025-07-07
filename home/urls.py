from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('cadastro/sucesso/', views.cadastro_success, name='cadastro_success'), # NOVA LINHA
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('produtos/', views.lista_produtos, name='lista_produtos'),
    path('produtos/adicionar/', views.adicionar_produto, name='adicionar_produto'),
    path('produtos/editar/<int:pk>/', views.editar_produto, name='editar_produto'),
    path('produtos/excluir/<int:pk>/', views.excluir_produto, name='excluir_produto'),
]