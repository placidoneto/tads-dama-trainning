from rest_framework import serializers
from api.models import Relato 

class RelatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relato  
        fields = "__all__"

        read_only_fields = ['relato_id', 'data_criacao', 'usuario'] 