# views.py

from rest_framework import viewsets, permissions
from api.models import Conversa
from api.serializers.conversa import ConversaSerializer

class ConversaViewSet(viewsets.ModelViewSet):
    queryset = Conversa.objects.all()
    serializer_class = ConversaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
    
        return Conversa.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)
