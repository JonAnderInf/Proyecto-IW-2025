
from django.shortcuts import render
from .models import Empleado, Equipo, Ticket

def lista_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'lista_empleados.html', {'empleados': empleados})

def lista_tickets(request):
    tickets = Ticket.objects.prefetch_related('equipos').all()
    return render(request, 'lista_tickets.html', {'tickets': tickets})