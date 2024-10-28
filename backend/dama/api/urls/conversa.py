from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views.conversa import ConversaViewSet

router = DefaultRouter()
router.register(r'conversas', ConversaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
