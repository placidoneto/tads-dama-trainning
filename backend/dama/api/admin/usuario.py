from django.contrib import admin
from api.models import Usuario  

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'eh_ong', 'ativo', 'administrador')  
    list_filter = ('eh_ong', 'ativo', 'administrador') 
    search_fields = ('nome', 'email') 
    ordering = ('nome') 
