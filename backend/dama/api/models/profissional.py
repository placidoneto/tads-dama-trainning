import uuid
from django.db import models

class Profissional(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    nome = models.CharField(max_length=100)
    
    estado_crp = models.CharField(max_length=2, editable=False)
    
    numero_crp = models.CharField(max_length=5, editable=False)
    
    email = models.EmailField(max_length=60)
    
    contato = models.CharField(max_length=60)
    
    data_criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Profissional'

        verbose_name_plural = 'Profissionais'

        ordering = ['nome']

        db_table = 'profissionais'

    def __str__(self) -> str:
        return f"Nome:{self.nome} CRP:{self.estado_crp}/{self.numero_crp}"

    