from api.models import profissional
from rest_framework import serializers


class ProfissionalSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = 'Profissional'

        fields = ['id', 'nome', 'estado_crp', 'numero_crp', 'email', 'contato', 'data_criacao']

        read_only_fields = ['id', 'data_criacao']
    
    # def create(self, validated_data):
    #     crp_base = validated_data.pop('crp_input')

    

