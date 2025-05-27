from django.shortcuts import render, redirect
from django.urls import reverse_lazy  
from .models import Empleado, Equipo, Ticket
from .forms import TicketForm, EmpleadoForm, EquipoForm
from django.views.generic import ListView, DeleteView, DetailView, CreateView, UpdateView

# ---------------------------------------------------------------------------------------AYAX CAMBIO DE ESTADO IMPORTS--------------------------------------------------------------------
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import get_object_or_404


# ---------------------------------------------------------------------------------------Logger--------------------------------------------------------------------------------------------------
import logging
logger = logging.getLogger('proyecto')


# ----------------------------------------------------------------------------------- VISTAS DE EMPLEADOS-----------------------------------------------------------------------------------------                         


# Vista para listar empleados
class ListaEmpleados(ListView):
    model = Empleado
    template_name = 'lista_empleados.html'
    context_object_name = 'empleados' 


# Vista de detalle de los empleados
class DetalleEmpleado(DetailView):
    model = Empleado
    template_name = 'detalles_empleado.html'
    context_object_name = 'empleado'


# Vista de creación de empleados
class CrearEmpleado(CreateView):
    template_name = 'crear_empleado.html'
    form_class = EmpleadoForm
    model = Empleado
    success_url = reverse_lazy('lista-empleados')

    def form_valid(self, form):
        response = super().form_valid(form)
        empleado = form.instance
        logger.info(f" Empleado creado: {empleado.nombre} {empleado.apellidos}")
        return response

class EliminarEmpleado(DeleteView):
    model = Empleado
    template_name = 'eliminar_empleado.html'
    success_url = reverse_lazy('lista-empleados')

    def delete(self, request, *args, **kwargs):
        empleado = self.get_object()
        logger.warning(f" Empleado eliminado: {empleado.nombre} {empleado.apellido}")
        return super().delete(request, *args, **kwargs)


# Vista de modificación de empleados
class ModificarEmpleado(UpdateView):
    model = Empleado
    template_name = 'modificar_empleado.html'
    form_class = EmpleadoForm
    success_url = reverse_lazy('lista-empleados')

    def form_valid(self, form):
        response = super().form_valid(form)
        empleado = form.instance
        logger.info(f" Empleado modificado: {empleado.nombre} {empleado.apellidos}")
        return response





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





# ---------------------------------------------------------------------------------------AYAX CAMBIO DE ESTADO / PRUEBA DE TOKEN UTILIZAMOS csrf_exempt -----------------------------------------------------------

@csrf_exempt 
def cambiar_estado_ticket(request, pk):
    if request.method == 'POST':
        ticket = get_object_or_404(Ticket, pk=pk)
        if ticket.estado == 'abierto':
            ticket.estado = 'cerrado'
        else:
            ticket.estado = 'abierto'
        ticket.save()
        return JsonResponse({'success': True, 'nuevo_estado': ticket.estado})
    return JsonResponse({'success': False}, status=400)
