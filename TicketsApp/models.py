# models.py
from django.db import models

class EstadoTicket(models.Model):
    nome = models.CharField(max_length=50)


class EstadoAtendimento(models.Model):
    nome = models.CharField(max_length=50)
    
class Ticket(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    estado_ticket = models.ForeignKey(EstadoTicket, on_delete=models.CASCADE)
    estado_atendimento = models.ForeignKey(EstadoAtendimento, on_delete=models.CASCADE)

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

