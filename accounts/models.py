from django.db import models
from django.contrib.auth.models import User


class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profissão = models.CharField(default='', max_length=50)
    cidade = models.CharField(default='', max_length=50)

