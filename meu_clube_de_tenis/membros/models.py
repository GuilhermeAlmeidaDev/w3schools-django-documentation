from django.db import models

class Membro(models.Model):
    
    primeiro_nome = models.CharField(max_length=255)
    ultimo_nome = models.CharField(max_length=255)
    telefone = models.IntegerField(null=True)
    entrou_em = models.DateTimeField(null=True)

    def __str__(self):
        return f"{self.primeiro_nome} {self.ultimo_nome}"
