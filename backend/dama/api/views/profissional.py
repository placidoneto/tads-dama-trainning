from rest_framework import viewsets
from api.models.profissional import Profissional 
from api.serializers.profissional import ProfissionalSerializer 


class ProfissionalViewSet(viewsets.ModelViewSet):
    queryset = Profissional.objects.all()
    serializer_class = ProfissionalSerializer