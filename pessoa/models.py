from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    idade = models.IntegerField()
    nacionalidade = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.nome} {self.sobrenome}"