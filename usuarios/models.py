from django.db import models



class Usuario(models.Model):
    usuario = models.CharField(max_length=30)
    email = models.EmailField()
    senha = models.CharField(max_length=20)
    confirmar_senha = models.CharField(max_length=20)

    def __str__(self):
        return self.usuario
