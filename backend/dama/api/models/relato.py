from django.utils import timezone
from django.db import models
from api.models.usuario import Usuario
import uuid


class Relato(models.Model):
    relato_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    relato_texto = models.TextField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "Relato"
        verbose_name_plural = "Relatos"
        ordering = ["relato_id"]
        db_table = "relato"

    def __str__(self):
        return self.relato_texto
    
    def update_texto(self, relato_texto=None):
        if relato_texto:
            self.relato_texto = relato_texto
        self.save()