from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    login = models.CharField(max_length=20, unique=True)
    senha = models.CharField(max_length=128)

    def __str__(self):
        return self.nome