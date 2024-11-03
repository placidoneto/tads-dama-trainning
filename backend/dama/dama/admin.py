from django.contrib import admin
from api.models.usuario import Usuario
from api.models.ong import ONG
from api.models.relato import Relato




admin.site.register(ONG)
admin.site.register(Usuario)
admin.site.register(Relato)