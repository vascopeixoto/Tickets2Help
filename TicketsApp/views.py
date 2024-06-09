from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import SoftwareTicket, HardwareTicket, EstadoTicket, EstadoAtendimento
from django.contrib.auth.decorators import login_required


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
    software_tickets = list(SoftwareTicket.objects.filter(user=user))
    hardware_tickets = list(HardwareTicket.objects.filter(user=user))

    for ticket in software_tickets:
        ticket.tipo = 'Software'

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