from django.contrib import admin
from core.models import Evento

# Register your models here.

# Altera como será mostrado no Painel Admin
class EventoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'data_evento', 'data_criacao', 'usuario')
    list_filter = ('usuario', 'data_evento',) # cria um filtro, sempre deixar a virgula no final

admin.site.register(Evento, EventoAdmin)