from rest_framework import serializers
from api.models import Usuario
from api.permissions import todos

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        
        model = Usuario

        fields = [
            'id', 'nome', 'email', 'eh_ong', 'data_criacao', 'data_atualizacao', 'ativo', 'administrador'
        ]
