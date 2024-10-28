from django.db import models
from django.conf import settings  
from django.utils import timezone

class Conversa(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name="conversas"
    )
    mensagem_usuario = models.TextField()  
    resposta_chatbot = models.TextField() 
    data_hora = models.DateTimeField(default=timezone.now)  

    emocao = models.CharField(max_length=50, null=True, blank=True)  
    intensidade_emocao = models.IntegerField(null=True, blank=True)  
    intencao_usuario = models.CharField(max_length=100, null=True, blank=True) 
    tipo_interacao = models.CharField(max_length=50, choices=[
        ('informativa', 'Informativa'),
        ('suporte_emocional', 'Suporte Emocional'),
        ('consulta', 'Consulta'),
        ('outro', 'Outro')
    ], default='outro')  
    duracao_resposta = models.DurationField(null=True, blank=True)  
    contexto_conversa = models.JSONField(null=True, blank=True)  
    acompanhamento = models.BooleanField(default=False)  
    avaliacao_usuario = models.IntegerField(null=True, blank=True) 

    class Meta:
        verbose_name = "Conversa"
        verbose_name_plural = "Conversas"
        ordering = ["-data_hora"]  

    def __str__(self):
        return f"Conversa de {self.usuario} em {self.data_hora.strftime('%Y-%m-%d %H:%M:%S')}"
