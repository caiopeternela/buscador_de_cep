from django.db import models

# Create your models here.
class Endereco(models.Model):
    cep = models.CharField(max_length=8, unique=True)
    cidade = models.CharField(max_length=128)
    bairro = models.CharField(max_length=128)
    logradouro = models.CharField(max_length=256)
    complemento = models.CharField(max_length=256, null=True, blank=True)