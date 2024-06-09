from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import SoftwareTicket, HardwareTicket, EstadoTicket, EstadoAtendimento
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.utils.timezone import now
from math import floor
from collections import defaultdict

def custom_login(request):
    if request.user.is_authenticated:
        print("Usuário já autenticado:", request.user)
        return redirect('tickets')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('tickets')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def custom_logout(request):
    logout(request)
    return redirect('login')


@login_required
def lista_tickets(request):
    user = request.user
    if user.is_staff:
        software_tickets = list(SoftwareTicket.objects.all())
        hardware_tickets = list(HardwareTicket.objects.all())
    else:
        software_tickets = list(SoftwareTicket.objects.filter(user=user))
        hardware_tickets = list(HardwareTicket.objects.filter(user=user))

    for ticket in software_tickets:
        ticket.tipo = 'Software'
    for ticket in hardware_tickets:
        ticket.tipo = 'Hardware'

    tickets = software_tickets + hardware_tickets

    tickets.sort(key=lambda x: x.created_at, reverse=True)

    context = {
        'tickets': tickets
    }
    return render(request, 'tickets.html', context)


@login_required
def adicionar_ticket(request):
    if request.method == 'POST':
        tipo_ticket = request.POST.get('tipoTicket')
        title = request.POST.get('title')
        description = request.POST.get('description')
        estado_ticket = EstadoTicket.objects.first()

        if tipo_ticket == 'software':
            software = request.POST.get('software')
            necessidade_desc = request.POST.get('necessidadeDesc')
            SoftwareTicket.objects.create(
                title=title,
                description=description,
                estado_ticket=estado_ticket,
                user=request.user,
                software=software,
                necessidadeDesc=necessidade_desc
            )
        elif tipo_ticket == 'hardware':
            equipamento = request.POST.get('equipamento')
            avaria = request.POST.get('avaria')
            HardwareTicket.objects.create(
                title=title,
                description=description,
                estado_ticket=estado_ticket,
                user=request.user,
                equipamento=equipamento,
                avaria=avaria
            )
        return redirect('lista_tickets')
    return render(request, 'tickets/adicionar_ticket.html')


def ticket_edit_details(request, tipo, ticket_id):
    ticket = None
    if tipo == 'software':
        ticket = get_object_or_404(SoftwareTicket, id=ticket_id)
    elif tipo == 'hardware':
        ticket = get_object_or_404(HardwareTicket, id=ticket_id)

    estados_ticket = EstadoTicket.objects.all()
    estados_atendimento = EstadoAtendimento.objects.all()
    return render(request, 'tickets.html', {'tipo': tipo, 'ticket': ticket, 'estados_ticket': estados_ticket, 'estados_atendimento': estados_atendimento})


def editar_ticket(request, tipo, ticket_id):
    if tipo == 'software':
        ticket = get_object_or_404(SoftwareTicket, id=ticket_id)
    elif tipo == 'hardware':
        ticket = get_object_or_404(HardwareTicket, id=ticket_id)

    if request.method == 'POST':
        if tipo == 'software':
            ticket.intervencaoDesc = request.POST.get('intervencaoDesc')
            ticket.estado_ticket_id = request.POST.get('estado_ticket')
            ticket.estado_atendimento_id = request.POST.get('estado_atendimento')
        elif tipo == 'hardware':
            ticket.reparacaoDesc = request.POST.get('reparacaoDesc')
            ticket.pecas = request.POST.get('pecas')
            ticket.estado_ticket_id = request.POST.get('estado_ticket')
            ticket.estado_atendimento_id = request.POST.get('estado_atendimento')

        ticket.save()

        return redirect('lista_tickets')
    else:
        return redirect('lista_tickets')

def hardware_estado_ticket_doughnut_chart(request):
    estados = EstadoTicket.objects.all()
    
    # Prepare data for the chart
    labels = []
    data = []

    for estado in estados:
        labels.append(estado.nome)
        count = HardwareTicket.objects.filter(estado_ticket=estado).count()
        data.append(count)

    chart_data = {
        'labels': labels,
        'data': data,
    }
    
    return JsonResponse(chart_data)

def hardware_estado_atendimento_doughnut_chart(request):
    estados = EstadoAtendimento.objects.all()
    
    # Prepare data for the chart
    labels = []
    data = []

    for estado in estados:
        labels.append(estado.nome)
        count = HardwareTicket.objects.filter(estado_atendimento=estado).count()
        data.append(count)

    chart_data = {
        'labels': labels,
        'data': data,
    }
    
    return JsonResponse(chart_data)

def hardware_count_ticket_resolved_bar_chart(request):
    resolved_tickets = HardwareTicket.objects.filter(resolved_at__isnull=False)
    day_counts = defaultdict(int)
    for ticket in resolved_tickets:
        time_difference = ticket.resolved_at - ticket.created_at
        days_difference = floor(time_difference.total_seconds() / 86400)  # 86400 seconds in a day
        day_counts[days_difference] += 1

    labels = sorted(day_counts.keys())
    data = [day_counts[day] for day in labels]
    chart_data = {
        'labels': labels,
        'data': data,
    }
    return JsonResponse(chart_data)