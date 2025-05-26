from django.shortcuts import render, redirect
from django.urls import reverse_lazy  
from .models import Empleado, Equipo, Ticket
from .forms import TicketForm, EmpleadoForm, EquipoForm
from django.views.generic import ListView, DeleteView, DetailView, CreateView, UpdateView


# ----------------------------------------------------------------------------VISTAS DE EMPLEADOS -----------------------------------------------------------------------------------------------------------------
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


# vista de eliminacion de empleados
class EliminarEmpleado(DeleteView):
    model = Empleado
    template_name = 'eliminar_empleado.html'
    success_url = reverse_lazy('lista-empleados')


# vista de modificacion de empleados
class ModificarEmpleado(UpdateView):
    model = Empleado
    template_name = 'modificar_empleado.html'
    form_class = EmpleadoForm
    success_url = reverse_lazy('lista-empleados')




#página principal
def home(request):
    return render(request, 'home.html')

# ----------------------------------------------------------------------------VISTAS DE TICKETS/FILTRO (1) -----------------------------------------------------------------------------------------------------------------
# vista de listar tickets
class ListaTickets(ListView):
    model = Ticket
    template_name = 'lista_tickets.html'
    context_object_name = 'tickets'

    def get_queryset(self):
        queryset = super().get_queryset()
        estado = self.request.GET.get('estado')

        if estado:
            queryset = queryset.filter(estado=estado)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['estados'] = Ticket.objects.values_list('estado', flat=True).distinct()
        return context

# vista de creación de tickets
class CrearTicket(CreateView):
    model = Ticket
    form_class = TicketForm
    template_name = 'crear_ticket.html'
    success_url = reverse_lazy('lista-tickets') 

# vista de detalles  de tickets
class DetalleTicket(DetailView):
    model = Ticket
    template_name = 'detalles_ticket.html'
    context_object_name = 'ticket'

# vista de modificación de tickets
class ModificarTicket(UpdateView):
    model = Ticket
    form_class = TicketForm
    template_name = 'modificar_ticket.html'
    success_url = reverse_lazy('lista-tickets')

# vista de eliminación de tickets
class EliminarTicket(DeleteView):
    model = Ticket
    template_name = 'eliminar_ticket.html'
    success_url = reverse_lazy('lista-tickets')






# ----------------------------------------------------------------------------VISTAS DE EQUIPOS/FILTRO (2) -----------------------------------------------------------------------------------------------------------------

# vista de listar equipos
class ListaEquipos(ListView):
    model = Equipo
    template_name = 'lista_equipos.html'
    context_object_name = 'equipos'

    def get_queryset(self):
        queryset = super().get_queryset()
        marca = self.request.GET.get('marca')
        tipo = self.request.GET.get('tipo')

        if marca:
            queryset = queryset.filter(marca=marca)
        if tipo:
            queryset = queryset.filter(tipo=tipo)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['marcas'] = Equipo.objects.values_list('marca', flat=True).distinct()
        context['tipos'] = Equipo.objects.values_list('tipo', flat=True).distinct()
        return context


# Detalle de equipos
class DetalleEquipo(DetailView):
    model = Equipo
    template_name = 'detalles_equipo.html'
    context_object_name = 'equipo'


# Crear equipos
class CrearEquipo(CreateView):
    model = Equipo
    template_name = 'crear_equipo.html'
    form_class = EquipoForm
    success_url = reverse_lazy('lista-equipos')


# Eliminar equipos
class EliminarEquipo(DeleteView):
    model = Equipo
    template_name = 'eliminar_equipo.html'
    success_url = reverse_lazy('lista-equipos')


# Modificar equipos
class ModificarEquipo(UpdateView):
    model = Equipo
    template_name = 'modificar_equipo.html'
    form_class = EquipoForm
    success_url = reverse_lazy('lista-equipos')






