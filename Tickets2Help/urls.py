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
from TicketsApp.views import lista_tickets, adicionar_ticket, ticket_details, editar_ticket, ticket_edit_details

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login'), name='logout'),
    path('tickets/', lista_tickets, name='lista_tickets'),
    path('', lista_tickets, name='lista_tickets'),
    path('adicionar_ticket/', adicionar_ticket, name='adicionar_ticket'),
    path('editdetailsticket/<str:tipo>/<int:ticket_id>/', ticket_edit_details, name='ticket_edit_details'),
    path('detailsticket/<str:tipo>/<int:ticket_id>/', ticket_details, name='ticket_details'),
    path('editar_ticket/<int:ticket_id>/', editar_ticket, name='editar_ticket'),

]
