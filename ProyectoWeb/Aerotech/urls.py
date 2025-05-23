from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Empleados
    path('lista_empleado/', views.ListaEmpleados.as_view(), name='lista-empleados'),
    path('crear_empleado/', views.CrearEmpleado.as_view(), name='crear-empleado'),
    path('empleado/<int:pk>/', views.DetalleEmpleado.as_view(), name='detalles-empleado'),
    path('empleado/<int:pk>/eliminar/', views.EliminarEmpleado.as_view(), name='eliminar-empleado'),
    path('empleado/<int:pk>/modificar/', views.ModificarEmpleado.as_view(), name='modificar-empleado'),

    # Equipos 
    path('equipos/', views.ListaEquipos.as_view(), name='lista-equipos'),
    path('crear_equipo/', views.CrearEquipo.as_view(), name='crear-equipo'),
    path('equipo/<int:pk>/', views.DetalleEquipo.as_view(), name='detalles-equipo'),
    path('equipo/<int:pk>/eliminar/', views.EliminarEquipo.as_view(), name='eliminar-equipo'),
    path('equipo/<int:pk>/modificar/', views.ModificarEquipo.as_view(), name='modificar-equipo'),

    # Tickets 
    path('tickets/', views.lista_tickets, name='lista_tickets'),
    path('crear_ticket/', views.crear_ticket, name='crear_ticket'),
]
