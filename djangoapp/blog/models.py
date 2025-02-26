from django.db import models
from django.urls import reverse

class Postagem(models.Model):
    titulo = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    categoria = models.ForeignKey('Categoria', on_delete=models.PROTECT)
    corpo = models.TextField()
    data = models.DateField(db_index=True, auto_now_add=True)


class Categoria(models.Model):
    titulo = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
