from rest_framework.routers import DefaultRouter
from api.views.relato import RelatoViewSet

relato_router = DefaultRouter()
relato_router.register("relato", RelatoViewSet, basename="relato")
