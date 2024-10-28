from rest_framework.routers import DefaultRouter

from api.views.usuario import UsuarioViewSet

usuario_router = DefaultRouter()
usuario_router.register("usuario", UsuarioViewSet, basename="usuario")
