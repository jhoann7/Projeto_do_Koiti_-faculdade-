from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    login = models.CharField(max_length=20, unique=True)
    senha = models.CharField(max_length=128)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=200, help_text="Nome do produto.")
    descricao = models.TextField(blank=True, null=True, help_text="Descrição detalhada do produto.")
    quantidade = models.IntegerField(default=0, help_text="Quantidade atual em estoque.")
    preco = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, help_text="Preço unitário do produto.")
    data_entrada = models.DateTimeField(auto_now_add=True, help_text="Data em que o produto foi registrado.")
    ultima_atualizacao = models.DateTimeField(auto_now=True, help_text="Última vez que as informações do produto foram atualizadas.")

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ['nome'] # Ordenar produtos pelo nome por padrão

    def __str__(self):
        return self.nome