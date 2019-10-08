from django.db import models


class Titulo(models.Model):

    class Meta:

        db_table = 'titulo'

    nome = models.CharField(max_length=200)
    vencimento = models.CharField(max_length=200)
    taxa_rendimento = models.CharField(max_length=200)
    valor_minimo = models.CharField(max_length=200)
    preco = models.CharField(max_length=200)

    def __str__(self):
        return self.nome