from django.contrib import admin
from api.models import ONG  

class ONGAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'responsavel', 'localizacao', 'ativo', 'data_criacao')  
    list_filter = ('ativo', 'tipo_servico')  
    search_fields = ('nome', 'responsavel','localizacao','tipo_servico')  
    ordering = ('data_criacao',)  


admin.site.register(ONG, ONGAdmin)
