from django.contrib import admin
from api.models.relato import Relato  

class RelatoAdmin(admin.ModelAdmin):
    list_display = ("relato_id", "relato_texto", "usuario", "data_criacao")
    list_filter = ("data_criacao", "usuario") 
    search_fields = ("usuario__nome", "usuario__email")
    ordering = ("relato_id")

