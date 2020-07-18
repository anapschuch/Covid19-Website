from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
    nome = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=200)
    idade = models.IntegerField(null=True)
    temperatura_maxima = models.FloatField(null=True)
    data_inicio_sintomas = models.DateField(null=True)

    def __str__(self):
        return self.nome

