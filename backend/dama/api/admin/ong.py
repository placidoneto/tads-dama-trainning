from api.models import ONG  
from django.contrib import admin

class ONGAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'responsavel', 'localizacao', 'ativo', 'data_criacao')  
    list_filter = ('ativo', 'tipo_servico')  
    search_fields = ('nome', 'responsavel','localizacao','tipo_servico')  
    ordering = ('data_criacao',)  

