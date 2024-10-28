from rest_framework.routers import DefaultRouter
from api.views.ong import ONGViewSet

ong_router = DefaultRouter()
ong_router.register("ong", ONGViewSet, basename="ong")
