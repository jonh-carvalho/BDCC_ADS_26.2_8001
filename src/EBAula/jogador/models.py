from django.db import models

class Jogador(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
