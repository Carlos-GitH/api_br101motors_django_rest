from django.contrib import admin
from api_br101motors.models import Agendamento, Motos, Proprietario 

# Register your models here.
class MotosAdmin(admin.ModelAdmin):
    list_display       = ('marca', 'modelo', 'cor', 'ano', 'proprietario_id', 'placa', 'data_cadastro', 'kilometragem')
    list_display_links = ('placa',)
    search_fields      = ('moto', 'proprietario_id', 'placa')
    list_per_page      = 20
    
admin.site.register(Motos, MotosAdmin)

class Proprietarios(admin.ModelAdmin):
    list_display       = ('id', 'nome', 'email', 'telefone', 'data_cadastro', 'cep', 'logradouro', 'bairro', 'numero', 'complemento', 'uf', 'municipio')
    list_display_links = ('id', 'nome')
    search_fields      = ('nome', 'email', 'placa')
    list_per_page      = 20
    
admin.site.register(Proprietario, Proprietarios)

class Agendamentos(admin.ModelAdmin):
    list_display       = ('data', 'servicos', 'proprietario_id', 'moto_id', 'status', 'data_solicitacao')
    list_display_links = ('data', 'servicos', 'status', 'moto_id',)
    search_fields      = ('proprietario_id', 'moto_id')
    list_per_page      = 20
    
admin.site.register(Agendamento, Agendamentos)