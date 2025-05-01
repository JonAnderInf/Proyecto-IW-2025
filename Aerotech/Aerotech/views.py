from django.shortcuts import render, redirect
from .models import Empleado, Equipo, Ticket
from .forms import TicketForm, EmpleadoForm, EquipoForm

def lista_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'lista_empleados.html', {'empleados': empleados})

def lista_tickets(request):
    tickets = Ticket.objects.select_related('empleado').prefetch_related('equipo').all()
    return render(request, 'lista_tickets.html', {'tickets': tickets})

def lista_equipos(request):
    equipos = Equipo.objects.all()
    return render(request, 'lista_equipos.html', {'equipos': equipos})



def crear_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_tickets')
    else:
        form = TicketForm()
    return render(request, 'Aerotech/crear_ticket.html', {'form': form})

def crear_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_empleados')
    else:
        form = EmpleadoForm()
    return render(request, 'Aerotech/crear_empleado.html', {'form': form})

def crear_equipo(request):
    if request.method == 'POST':
        form = EquipoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_equipos')
    else:
        form = EquipoForm()
    return render(request, 'Aerotech/crear_equipo.html', {'form': form})
