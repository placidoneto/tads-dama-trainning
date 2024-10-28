from django.contrib import admin
from api.models import *

from .ong import ONGAdmin
from .usuario import UsuarioAdmin

admin.site.register(ONG, ONGAdmin)
admin.site.register(Usuario, UsuarioAdmin)