#from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from api.models import ONG
from rest_framework.permissions import IsAuthenticated
from api.permissions.todos import TodosPodemCriar, TodosPodemVer
from api.serializers.ong import ONG


class ONGViewSet(viewsets.ModelViewSet):
    serializer_class = ONG
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    #filter_backends = [DjangoFilterBackend]
    permission_classes = [IsAuthenticated & (TodosPodemCriar | TodosPodemVer)]
    queryset = ONG.objects.all()

