from django.urls import include, path, re_path
from .usuario import usuario_router
from .ong import ong_router

urlpatterns = [
    path('api/', include(usuario_router.urls)),
    path('api/', include(ong_router.urls)),
]
