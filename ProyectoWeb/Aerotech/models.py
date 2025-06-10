from django.db import models

class Empleado(models.Model):
    dni = models.CharField(max_length=9, unique=True)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=150)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    username = models.CharField(max_length=150, unique=True, null=True, blank=True)



    def __str__(self):
        return f" Nombre {self.nombre} Apellidos {self.apellidos}"
    
class Proveedor(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre
    
class Equipo(models.Model):
    MODELOS = [
        ('1', 'aaaaaa000'),
        ('2', 'aaaaaaa111'),
        ('3', 'aaaaaaa999'),
        ('4', 'aaaaaaa888'),
    ]

    MARCAS = [
        ('1', 'Ikertronic'),
        ('2', 'JonAndertech'),
    ]

    TIPOS = [
        ('1', 'Deshumidificador de Aire'),
        ('2', 'Depuradora'),
        ('3', 'Aire Acondicionado'),
    ]
        
    numero_serie = models.CharField(max_length=100, unique=True)
    modelo = models.CharField(max_length=50, choices=MODELOS)
    marca = models.CharField(max_length=50, choices=MARCAS)
    tipo = models.CharField(max_length=50, choices=TIPOS)
    fecha_adquisicion = models.DateField()
    fecha_puesta_marcha = models.DateField()
    proveedores = models.ManyToManyField(Proveedor, related_name='equipos')
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
    empleado = models.ForeignKey(Empleado, on_delete=models.SET_NULL, null=True) 
    equipos = models.ManyToManyField(Equipo) 

    def __str__(self):
        return f"{self.titulo} - {self.referencia}"  