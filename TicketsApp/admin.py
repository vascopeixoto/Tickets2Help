from django.contrib import admin
from .models import SoftwareTicket, HardwareTicket, EstadoTicket, EstadoAtendimento


@admin.register(SoftwareTicket)
class SoftwareTicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'estado_ticket', 'estado_atendimento', 'created_at')


@admin.register(HardwareTicket)
class HardwareTicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'estado_ticket', 'estado_atendimento', 'created_at')


@admin.register(EstadoTicket)
class EstadoTicketAdmin(admin.ModelAdmin):
    list_display = ('nome',)


@admin.register(EstadoAtendimento)
class EstadoAtendimentoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
