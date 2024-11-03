from rest_framework.routers import DefaultRouter
from api.views.profissional import ProfissionalViewSet


router_profissional = DefaultRouter()
router_profissional.register(r'profissional', ProfissionalViewSet)

