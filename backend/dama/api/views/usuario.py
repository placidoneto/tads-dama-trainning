#from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from api.models import Usuario
from rest_framework.permissions import IsAuthenticated
from api.permissions.todos import TodosPodemCriar
from api.serializers.usuario import UsuarioSerializer
from rest_framework.authentication import TokenAuthentication



class UsuarioViewSet(viewsets.ModelViewSet):
    serializer_class = UsuarioSerializer
    http_method_names = ['get', 'post']
    #filter_backends = [DjangoFilterBackend]
    permission_classes = [IsAuthenticated | TodosPodemCriar]
    authentication_classes = [TokenAuthentication] 
    queryset = Usuario.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)
