from rest_framework import serializers
from api.models import Conversa

class ConversaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversa
        fields = [
            'id', 'usuario', 'mensagem_usuario', 'resposta_chatbot', 'data_hora',
            'emocao', 'intensidade_emocao', 'intencao_usuario', 'tipo_interacao',
            'duracao_resposta', 'contexto_conversa', 'acompanhamento', 'avaliacao_usuario'
        ]
        read_only_fields = ['usuario', 'data_hora', 'resposta_chatbot']  

    def create(self, validated_data):
        
        validated_data['usuario'] = self.context['request'].user
        return super().create(validated_data)
