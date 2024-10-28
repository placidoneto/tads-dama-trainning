from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)
    eh_ong = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)
    administrador = models.BooleanField(default=False)
    ultimo_acesso = models.DateTimeField(null=True, blank=True)
    ultima_atualizacao_senha = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        ordering = ["nome"]
        db_table = "usuario"

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        if self.senha:
            self.senha = make_password(self.senha)  
        super().save(*args, **kwargs)

    def verificar_senha(self, senha):
        return check_password(senha, self.senha) 
