from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE



TIPO_VEICULO = [
    ('Carro','Carro'),
    ('Motocicleta','Motocicleta'),
    ('Caminhonete','Caminhonete'),
    ('Caminhão','Caminhão'),
    ('Ônibus','Ônibus'),
    ('Microônibus','Microônibus'),
    ('Triciclo','Triciclo'),
    ('Quadriciclo','Quadriciclo'),
    ('Reboque','Reboque'),
    ('Trator','Trator')
]


class Admin(models.Model):
    nome = models.CharField(max_length=32)
    sobrenome = models.CharField(max_length=32)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Administrador'
        verbose_name_plural = 'Administradores'

    def __str__(self):
        return '{} {}'.format(self.nome, self.sobrenome)

class Marca(models.Model):
    marca = models.CharField(max_length=64)
    
    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'
    
    def __str__(self):
        return self.marca

class Modelo(models.Model):
    modelo = models.CharField(max_length=64)
    marca = models.ForeignKey(Marca, on_delete=CASCADE, default=0)

    
    class Meta:
        verbose_name = 'Modelo'
        verbose_name_plural = 'Modelos'    
    
    def __str__(self):
        return '{} {}'.format(self.marca, self.modelo)

class Produto(models.Model):
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    ano = models.IntegerField(null=True)
    cilindrada = models.CharField(max_length=10,default='')
    km = models.IntegerField(null=True)
    cor = models.CharField(max_length=64)
    caracteristicas = models.TextField(null=True)
    tipo = models.CharField(max_length=16, choices=TIPO_VEICULO, default='Carro')
    preco = models.DecimalField(max_digits=10,decimal_places=2, default=0)
    capa = models.ImageField(null=True, blank=True)
    visitas = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['-id']

    def __str__(self):
        return '{} {} {}'.format(self.modelo,self.cilindrada,self.ano)
    
    def visita(self):
        self.visitas = self.visitas + 1