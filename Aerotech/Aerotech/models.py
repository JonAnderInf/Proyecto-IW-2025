from django.db import models

class Empleado(models.Model):
    dni = models.CharField(max_length=9, unique=True)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=150)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"
    

class Equipo(models.Model):
    numero_serie = models.CharField(max_length=100, unique=True)
    modelo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    fecha_adquisicion = models.DateField()
    fecha_puesta_marcha = models.DateField()
    proveedor_nombre = models.CharField(max_length=100)
    proveedor_telefono = models.CharField(max_length=15)
    planta = models.CharField(max_length=100)
    empleados = models.ManyToManyField(Empleado, related_name="equipos_asignados") 


def __str__(self):
        return f"{self.modelo} - {self.numero_serie}"

class Ticket(models.Model):
    referencia = models.CharField(max_length=100, unique=True)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_apertura = models.DateField(auto_now_add=True)
    fecha_resolucion = models.DateField(null=True, blank=True)
    urgencia = models.CharField(max_length=10, choices=[('alta', 'Alta'), ('media', 'Media'), ('baja', 'Baja')])
    tipo = models.CharField(max_length=15, choices=[('averia', 'Avería'), ('mejora', 'Mejora'), ('mantenimiento', 'Mantenimiento')])
    estado = models.CharField(max_length=10, choices=[('abierto', 'Abierto'), ('cerrado', 'Cerrado')])
    empleado_asignado = models.ForeignKey(Empleado, on_delete=models.SET_NULL, null=True)  # ONE TO MANY
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)  

    def __str__(self):
        return f"{self.titulo} - {self.referencia}"  