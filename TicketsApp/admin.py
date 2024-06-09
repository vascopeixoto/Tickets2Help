from django.contrib import admin
from .models import SoftwareTicket, HardwareTicket, EstadoTicket, EstadoAtendimento


class SoftwareTicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'estado_ticket', 'estado_atendimento', 'created_at', 'software') # Incluindo 'software'

class HardwareTicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'estado_ticket', 'estado_atendimento', 'created_at') # Se você também deseja incluir 'equipamento', adicione aqui.

class EstadoTicketAdmin(admin.ModelAdmin):
    list_display = ('nome',)

class EstadoAtendimentoAdmin(admin.ModelAdmin):
    list_display = ('nome',)


admin.site.register(SoftwareTicket, SoftwareTicketAdmin)
admin.site.register(HardwareTicket, HardwareTicketAdmin)

admin.site.register(EstadoTicket, EstadoTicketAdmin)
admin.site.register(EstadoAtendimento, EstadoAtendimentoAdmin)
