from django.shortcuts import render, redirect
from django.urls import reverse_lazy  
from .models import Empleado, Equipo, Ticket
from .forms import TicketForm, EmpleadoForm, EquipoForm
from django.views.generic import ListView, DeleteView, DetailView, CreateView, UpdateView


# VISTAS DE EMPLEADOS Vistas CON CLASES
# vista para listar empleados
class ListaEmpleados(ListView):
    model = Empleado
    template_name = 'lista_empleados.html'
    context_object_name = 'empleados'  # Nose si podemos poner 'empleado'


# vista de detalle de los empleados
class DetalleEmpleado(DetailView):
    model = Empleado
    template_name = 'detalles_empleado.html'
    context_object_name = 'empleado'


# vista de creacion de empleados
class CrearEmpleado(CreateView):
    template_name = 'crear_empleado.html'
    form_class = EmpleadoForm
    model = Empleado
    success_url = reverse_lazy('listar-empleados')


# vista de eliminacion de producto
class EliminarEmpleado(DeleteView):
    model = Empleado
    template_name = 'eliminar_empleado.html'
    success_url = reverse_lazy('listar-empleados')


# vista de modificacion de producto
class ModificarEmpleado(UpdateView):
    model = Empleado
    template_name = 'modificar_empleado.html'
    form_class = EmpleadoForm
    success_url = reverse_lazy('listar-empleados')


# Vistas sin CLASES
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





def index_view(request):
    return render(request, 'index.html')  # cualquier otra plantilla prueba ???
