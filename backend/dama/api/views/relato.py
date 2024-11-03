from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from api.models.relato import Relato
from api.serializers.relato import RelatoSerializer

class RelatoViewSet(viewsets.ModelViewSet):
    serializer_class = RelatoSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    filter_backends = [DjangoFilterBackend]
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    
    def get_queryset(self):
        return Relato.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        if not self.request.user.eh_ong:
            return Response({"detail": "Apenas ONGs podem criar relatos."}, status=status.HTTP_403_FORBIDDEN)
        serializer.save(usuario=self.request.user)

    def perform_update(self, serializer):
        if not self.request.user.eh_ong:
            return Response({"detail": "Apenas ONGs podem editar relatos."}, status=status.HTTP_403_FORBIDDEN)
        serializer.save()
