from django.db import models

class Produto(models.Model):

    nome = models.CharField ("Nome", max_length= 100)
    preco = models.DecimalField("Preço", max_digits=9, decimal_places=2)
    quantidade_disponivel = models.IntegerField("Quantidade Estoque")

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField("Nome", max_length=50)
    sobrenome = models.CharField("Sobrenome", max_length=200)
    email = models.CharField("email", max_length=100)

    def __str__(self):
        return self.nome

    