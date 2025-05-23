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
    context_object_name = 'empleados' 


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
    success_url = reverse_lazy('lista-empleados')


# vista de eliminacion de producto
class EliminarEmpleado(DeleteView):
    model = Empleado
    template_name = 'eliminar_empleado.html'
    success_url = reverse_lazy('lista-empleados')


# vista de modificacion de producto
class ModificarEmpleado(UpdateView):
    model = Empleado
    template_name = 'modificar_empleado.html'
    form_class = EmpleadoForm
    success_url = reverse_lazy('lista-empleados')


# Vistas sin CLASES

#página principal
def home(request):
    return render(request, 'home.html')

#lista tickets
def lista_tickets(request):
    tickets = Ticket.objects.select_related('empleado').prefetch_related('equipo').all()
    return render(request, 'lista_tickets.html', {'tickets': tickets})

#crear ticket
def crear_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_tickets')
    else:
        form = TicketForm()
    return render(request, 'crear_ticket.html', {'form': form})






# VISTAS DE EQUIPOS Vistas CON CLASES

# Listar equipos
class ListaEquipos(ListView):
    model = Equipo
    template_name = 'lista_equipos.html'
    context_object_name = 'equipos'


# Detalle de equipo
class DetalleEquipo(DetailView):
    model = Equipo
    template_name = 'detalles_equipo.html'
    context_object_name = 'equipo'


# Crear equipo
class CrearEquipo(CreateView):
    model = Equipo
    template_name = 'crear_equipo.html'
    form_class = EquipoForm
    success_url = reverse_lazy('lista-equipos')


# Eliminar equipo
class EliminarEquipo(DeleteView):
    model = Equipo
    template_name = 'eliminar_equipo.html'
    success_url = reverse_lazy('lista-equipos')


# Modificar equipo
class ModificarEquipo(UpdateView):
    model = Equipo
    template_name = 'modificar_equipo.html'
    form_class = EquipoForm
    success_url = reverse_lazy('lista-equipos')






