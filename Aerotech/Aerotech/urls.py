from django.urls import path
from . import views

urlpatterns = [
    path('empleados/', views.lista_empleados, name='lista_empleados'),
    path('tickets/', views.lista_tickets, name='lista_tickets'),
    path('equipos/', views.lista_equipos, name='lista_equipos'),

    path('crear_ticket/', views.crear_ticket, name='crear_ticket'),
    path('crear_empleado/', views.crear_empleado, name='crear_empleado'),
    path('crear_equipo/', views.crear_equipo, name='crear_equipo'),
]
