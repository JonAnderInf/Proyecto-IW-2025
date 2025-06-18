from django.shortcuts import render, redirect
from django.urls import reverse_lazy  
from .models import Empleado, Equipo, Ticket
from .forms import TicketForm, EmpleadoForm, EquipoForm
from django.views.generic import ListView, DeleteView, DetailView, CreateView, UpdateView
from django.contrib import messages



# --------------------------------------------------------------------------------------- CAMBIO DE ESTADO FETCH/POST--------------------------------------------------------------------
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
import json

# ---------------------------------------------------------------------------------------LOGGER--------------------------------------------------------------------------------------------------
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
    
    def dispatch(self, request, *args, **kwargs):  # Prueba para el logger y protección de navegación
        if "empleado_id" not in request.session:
            return redirect("login-empleado")
        return super().dispatch(request, *args, **kwargs)
        

    


# Vista de creación de empleados
class CrearEmpleado(CreateView):
    template_name = 'crear_empleado.html'
    form_class = EmpleadoForm
    model = Empleado
    success_url = reverse_lazy('lista-empleados')


    def dispatch(self, request, *args, **kwargs):  # Prueba para el logger y protección de navegación
        if "empleado_id" not in request.session:
            return redirect("login-empleado")
        return super().dispatch(request, *args, **kwargs)

    

    def form_valid(self, form):
        response = super().form_valid(form)
        empleado = form.instance
        logger.info(f" Empleado creado: {empleado.nombre} {empleado.apellidos}")
        messages.success(self.request, "Creado")

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


    
    def dispatch(self, request, *args, **kwargs):  # Prueba para el logger y protección de navegación
        if "empleado_id" not in request.session:
            return redirect("login-empleado")
        return super().dispatch(request, *args, **kwargs)

    


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        estados = Ticket.objects.values_list('estado', flat=True)
        context['estados'] = list(set(estados)) 
        return context




# vista de creación de tickets
class CrearTicket(CreateView):
    model = Ticket
    form_class = TicketForm
    template_name = 'crear_ticket.html'
    success_url = reverse_lazy('lista-tickets') 

    
    def dispatch(self, request, *args, **kwargs):  # Prueba para el logger y protección de navegación
        if "empleado_id" not in request.session:
            return redirect("login-empleado")
        return super().dispatch(request, *args, **kwargs)

    

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


    
    def dispatch(self, request, *args, **kwargs):  # Prueba para el logger y protección de navegación
        if "empleado_id" not in request.session:
            return redirect("login-empleado")
        return super().dispatch(request, *args, **kwargs)

    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        marcas = Equipo.objects.values_list('marca', flat=True) 
        tipos = Equipo.objects.values_list('tipo', flat=True) 

        context['marcas'] = list(set(marcas))
        context['tipos'] = list(set(tipos))

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


    
    def dispatch(self, request, *args, **kwargs):  # Prueba para el logger y protección de navegación
        if "empleado_id" not in request.session:
            return redirect("login-empleado")
        return super().dispatch(request, *args, **kwargs)

    

    


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





# --------------------------------------------------------------------------------------- CAMBIO DE ESTADO DE TICKET -----------------------------------------------------------

def cambiar_estado_ticket(request, pk):
    if request.method == "POST":
        ticket = get_object_or_404(Ticket, id=pk)
        ticket.estado = 'cerrado' if ticket.estado == 'abierto' else 'abierto'
        ticket.save()
        return JsonResponse({'success': True, 'nuevo_estado': ticket.estado})
    else:
        return JsonResponse({'success': False, 'error': 'Método no permitido'}, status=405)


# --------------------------------------------------------------------------------------- CREAR LOGGIN EMPLEADOS------------------------------------------------------------------


def login_empleado(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        try:
            empleado = Empleado.objects.get(username=username, password=password)
            request.session["empleado_id"] = empleado.id
            request.session["departamento"] = empleado.departamento
            return redirect("home")  # La vista del home en nuestro caso o sino la lista de empleados
        except Empleado.DoesNotExist:
            return render(request, "login-empleado.html", {"error": "Credenciales incorrectas"})
    
    return render(request, "login-empleado.html")

def logout_empleado(request):
    request.session.flush()
    return redirect("login-empleado")






def logout_empleado(request):
    request.session.flush()  # Borra los datos del empleado creado en este caso
    return redirect('login-empleado') 

