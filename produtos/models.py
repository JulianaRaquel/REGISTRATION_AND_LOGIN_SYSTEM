from django.db import models



class Categoria(models.Model):
    categoria = models.CharField(max_length=20)

    def __str__(self):
        return self.categoria


class Opcoes(models.Model):
    nome = models.CharField(max_length=100)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


class Adicional(models.Model):
    nome = models.CharField(max_length=20)
    opcoes = models.ManyToManyField(Opcoes)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome_produto = models.CharField(max_length=20)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    preco_unitario = models.FloatField()
    adicionais = models.BooleanField()
    adicoes = models.ManyToManyField(Adicional)
    quantidade = models.IntegerField()

    def __str__(self):
        return self.nome_produto
