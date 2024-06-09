from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import SoftwareTicket, HardwareTicket
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
