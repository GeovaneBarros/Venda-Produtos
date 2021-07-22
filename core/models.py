from django.db import models
from django.contrib.auth.models import User

class Admin(models.Model):
    nome = models.CharField(max_length=32)
    sobrenome = models.CharField(max_length=32)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Administrador'
        verbose_name_plural = 'Administradores'

    def __str__(self):
        return '{} {}'.format(self.nome, self.sobrenome)


class Modelo(models.Model):
    modelo = models.CharField(max_length=64)
    marca = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'Modelo'
        verbose_name_plural = 'Modelos'    
    
    def __str__(self):
        return '{} {}'.format(self.modelo,self.marca)

class Produto(models.Model):
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    ano = models.IntegerField(null=True)
    km = models.IntegerField(null=True)
    cor = models.CharField(max_length=64)
    caracteristicas = models.TextField(null=True)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return '{} {} {}'.format(self.modelo,self.ano,self.cor)
    