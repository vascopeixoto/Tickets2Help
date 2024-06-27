"""
URL configuration for Tickets2Help project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from TicketsApp.views import chat_ticket, lista_tickets, adicionar_ticket, download_software_tickets, editar_ticket, download_hardware_tickets, hardware_estado_ticket_doughnut_chart, hardware_estado_atendimento_doughnut_chart, hardware_count_ticket_resolved_bar_chart, software_estado_ticket_doughnut_chart, software_estado_atendimento_doughnut_chart, software_count_ticket_resolved_bar_chart

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login'), name='logout'),
    path('tickets/', lista_tickets, name='lista_tickets'),
    path('', lista_tickets, name='lista_tickets'),
    path('adicionar_ticket/', adicionar_ticket, name='adicionar_ticket'),
    path('editar_ticket/<str:tipo>/<int:ticket_id>/', editar_ticket, name='editar_ticket'),
    path('hardware-estado-ticket-doughnut-chart/', hardware_estado_ticket_doughnut_chart, name='hardware_estado_ticket_doughnut_chart'),
    path('hardware-estado-atendimento-doughnut-chart/', hardware_estado_atendimento_doughnut_chart, name='hardware_estado_atendimento_doughnut_chart'),   
    path('hardware-count-ticket-resolved-bar-chart/', hardware_count_ticket_resolved_bar_chart, name='hardware_count_ticket_resolved_bar_chart'), 
    path('software-estado-ticket-doughnut-chart/', software_estado_ticket_doughnut_chart, name='software_estado_ticket_doughnut_chart'),
    path('software-estado-atendimento-doughnut-chart/', software_estado_atendimento_doughnut_chart, name='software_estado_atendimento_doughnut_chart'),   
    path('software-count-ticket-resolved-bar-chart/', software_count_ticket_resolved_bar_chart, name='software_count_ticket_resolved_bar_chart'),   
    path('download/hardware/', download_hardware_tickets, name='download_hardware_tickets'),
    path('tickets/hardware-estado-ticket-doughnut-chart/', hardware_estado_ticket_doughnut_chart, name='hardware_estado_ticket_doughnut_chart'),
    path('tickets/hardware-estado-atendimento-doughnut-chart/', hardware_estado_atendimento_doughnut_chart, name='hardware_estado_atendimento_doughnut_chart'),   
    path('tickets/hardware-count-ticket-resolved-bar-chart/', hardware_count_ticket_resolved_bar_chart, name='hardware_count_ticket_resolved_bar_chart'), 
    path('tickets/software-estado-ticket-doughnut-chart/', software_estado_ticket_doughnut_chart, name='software_estado_ticket_doughnut_chart'),
    path('tickets/software-estado-atendimento-doughnut-chart/', software_estado_atendimento_doughnut_chart, name='software_estado_atendimento_doughnut_chart'),   
    path('tickets/software-count-ticket-resolved-bar-chart/', software_count_ticket_resolved_bar_chart, name='software_count_ticket_resolved_bar_chart'),   
    path('download/software/', download_software_tickets, name='download_software_tickets'),
    path('chat_ticket/<str:tipo>/<int:ticket_id>/', chat_ticket, name='chat_ticket'),
]
