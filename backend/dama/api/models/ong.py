from django.db import models
import uuid

class ONG(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=100)
    responsavel = models.CharField(max_length=200)
    contato_reponsavel = models.CharField(max_length=60)
    tipo_servico = models.CharField(max_length=100)
    localizacao = models.CharField(max_length=200)

    ativo = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        verbose_name = "ONG"
        verbose_name_plural = "ONGs"
        ordering = ["nome"]
        db_table = "ong"

    def __str__(self):
        return self.nome

    def verificar_ong(self):
        
        return self.ativo

    def update_informacoes(self, nome=None, tipo_servico=None, localizacao=None):
        if nome:
            self.nome = nome
        if tipo_servico:
            self.tipo_servico = tipo_servico
        if localizacao:
            self.localizacao = localizacao
        self.save()  
