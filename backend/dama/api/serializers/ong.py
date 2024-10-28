from rest_framework import serializers
from api.models import ONG 

class ONGSerializer(serializers.ModelSerializer):
    class Meta:
        model = ONG  
        fields = [
            'id', 'nome', 'responsavel', 'contato_reponsavel', 'tipo_servico', 'localizacao', 'ativo', 'data_criacao'
        ]
        
        read_only_fields = ['id', 'data_criacao'] 