from django.db import models

# Create your models here.

class Artigo(models.Model):

    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()
    categoria = models.CharField(max_length=50)
    tags = models.JSONField(default=list)
    criadoEm = models.DateTimeField(auto_now_add=True)
    editadoEm = models.DateField(auto_now=True)

    def __str__(self):
        return self.titulo