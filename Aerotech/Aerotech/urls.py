from django.urls import path
from . import views

urlpatterns = [
    path('Aerotech/', views.index_view, name='aerotech-index') # prueba 

    path('', views.ListaEmpleados.as_view(), name='listar-empleados'),
    path('crear_empleado/', views.CrearEmpleado.as_view(), name='crear-empleado'),
    path('empleado/<int:pk>/', views.DetalleEmpleado.as_view(), name='detalles-empleado'),
    path('empleado/<int:pk>/eliminar/', views.EliminarEmpleado.as_view(), name='eliminar-empleado'),
    path('empleado/<int:pk>/modificar/', views.ModificarEmpleado.as_view(), name='modificar-empleado'),

    path('crear_equipo/', views.crear_equipo, name='crear_equipo'),
    path('tickets/', views.lista_tickets, name='lista_tickets'),
    path('equipos/', views.lista_equipos, name='lista_equipos'),
    path('crear_ticket/', views.crear_ticket, name='crear_ticket'),
]
