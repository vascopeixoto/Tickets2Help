from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class EstadoTicket(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class EstadoAtendimento(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Ticket(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    estado_ticket = models.ForeignKey(EstadoTicket, on_delete=models.CASCADE)
    estado_atendimento = models.ForeignKey(EstadoAtendimento, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resolved_at = models.DateTimeField(null=True)
    resolved = models.BooleanField(null=True)

    class Meta:
        abstract = True


class SoftwareTicket(Ticket):
    software = models.TextField()
    necessidadeDesc = models.TextField()
    intervencaoDesc = models.TextField()


class HardwareTicket(Ticket):
    equipamento = models.TextField()
    avaria = models.TextField()
    reparacaoDesc = models.TextField()
    pecas = models.TextField()


class Message(models.Model):
    ticket_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    ticket_object_id = models.PositiveIntegerField()
    ticket = GenericForeignKey('ticket_content_type', 'ticket_object_id')
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


class SoftwareTicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'estado_ticket', 'estado_atendimento', 'created_at', 'software')  # Incluindo 'software'


class HardwareTicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'estado_ticket', 'estado_atendimento',
                    'created_at')  # Se você também deseja incluir 'equipamento', adicione aqui.


class EstadoTicketAdmin(admin.ModelAdmin):
    list_display = ('nome',)


class EstadoAtendimentoAdmin(admin.ModelAdmin):
    list_display = ('nome',)


admin.site.register(SoftwareTicket, SoftwareTicketAdmin)
admin.site.register(HardwareTicket, HardwareTicketAdmin)

admin.site.register(EstadoTicket, EstadoTicketAdmin)
admin.site.register(EstadoAtendimento, EstadoAtendimentoAdmin)
